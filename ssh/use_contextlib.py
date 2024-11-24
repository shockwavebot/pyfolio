from contextlib import contextmanager
from dataclasses import dataclass


@dataclass
class Connection:
    dest: str
    auth_type: str
    auth: str

    def __post_init__(self):
        print('Connection object created, connection still not established')

    def run_cmd(self, cmd: str):
        print(f'Executing command on remote host: {cmd}')

    def open(self):
        print('Connection opened')

    def close(self):
        print('Connection closed')


@contextmanager
def open(conn: Connection):
    conn.open()
    try:
        yield conn
    finally:
        conn.close()
