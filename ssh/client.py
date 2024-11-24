import os
from typing import Final, Optional

import paramiko
from pydantic import BaseModel, Field

from ssh.auth import Config as SshAuthConfig

SSH_CONNECTION_TIMEOUT: Final[int] = 7


class Result(BaseModel):
    """
    Class for representing result after command execution on remote host
    """
    stdout: str
    stderr: str
    rc: int

    def is_ok(self) -> bool:
        return self.rc == 0


class Connection(BaseModel):
    """
    SSH Connection management class using Paramiko

    Example:
    >>> config = {
    ...         "host": "54.219.159.188",
    ...         "username": "ec2-user",
    ...         "auth": {"key_filename": "/Users/me/my.pem"},
    ...     }
    >>> with SshConnection(**config) as conn:
    ...     conn.execute('uname -om')
    ...
    Result(stdout='x86_64 GNU/Linux', stderr='', rc=0)
    """
    host: str = Field(..., description="Remote host IP address or FQDN")
    username: str = Field(..., description="Remote host username")
    auth: SshAuthConfig = Field(..., description="SSH Authentication configuration")
    port: int = Field(default=22, ge=1, le=65535)
    timeout: int = Field(default=SSH_CONNECTION_TIMEOUT, ge=1, le=300)

    _client: Optional[paramiko.SSHClient] = None
    _connected: bool = False

    def __repr__(self) -> str:
        return f"Connection(host='{self.host}', port={self.port}, {self.auth})"

    def __enter__(self):
        if self._connected:
            raise RuntimeError("SSH connection already established")

        self._client = paramiko.SSHClient()
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            self._client.connect(
                hostname=self.host,
                port=self.port,
                username=self.username,
                timeout=self.timeout,
                **self.auth.model_dump()
            )
            self._connected = True
            return self
        except Exception as e:
            self._close()
            raise ConnectionError(f"Failed to establish SSH connection: {str(e)}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._close()

    def _close(self):
        if self._client:
            self._client.close()
            self._client = None
        self._connected = False

    def execute(self, command: str) -> Result:
        """
        Execute command on remote host
        """
        if not self._connected or not self._client:
            raise RuntimeError("Not connected. Use with context manager")

        try:
            _, stdout, stderr = self._client.exec_command(command)
            return_code = stdout.channel.recv_exit_status()

            return Result(
                stdout=stdout.read().decode('utf-8').strip(),
                stderr=stderr.read().decode('utf-8').strip(),
                rc=return_code
            )
        except Exception as e:
            raise RuntimeError(f"Failed to execute command: {str(e)}")

    def copy_file(self, local_path: str, remote_path: str) -> None:
        """
        Copy local file to remote host
        """
        if not self._connected or not self._client:
            raise RuntimeError("Not connected. Use with 'with' statement")

        if not os.path.exists(local_path):
            raise FileNotFoundError(f"Local file not found: {local_path}")

        try:
            sftp = self._client.open_sftp()
            try:
                sftp.put(local_path, remote_path)
            finally:
                sftp.close()
        except Exception as e:
            raise RuntimeError(f"Failed to copy file: {str(e)}")
