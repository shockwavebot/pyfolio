from pathlib import Path

import pytest

from ssh_connection.auth import SshAuthConfig


def test_valid_password_auth():
    config = SshAuthConfig(password="securepassword")
    assert config.password == "securepassword"
    assert config.key_path is None
    assert str(config) == "AuthConfig(type=password)"


def test_valid_key_path_auth(mocker):
    mocker.patch("pathlib.Path.exists", return_value=True)
    config = SshAuthConfig(key_path="~/.ssh/id_rsa")
    assert config.password is None
    assert config.key_path == "~/.ssh/id_rsa"
    assert str(config) == "AuthConfig(type=key)"


def test_invalid_key_path_auth(mocker):
    mocker.patch("pathlib.Path.exists", return_value=False)
    with pytest.raises(ValueError, match="SSH key not found: ~/.ssh/id_rsa"):
        SshAuthConfig(key_path="~/.ssh/id_rsa")


def test_both_password_and_key_path():
    with pytest.raises(ValueError, match="Cannot specify both password and key_path"):
        SshAuthConfig(password="securepassword", key_path="~/.ssh/id_rsa")


def test_neither_password_nor_key_path():
    with pytest.raises(ValueError, match="Either password or key_path must be provided"):
        SshAuthConfig()


def test_key_path_expansion_invalid(mocker):
    mocker.patch("pathlib.Path.exists", return_value=False)
    mocker.patch("pathlib.Path.expanduser", return_value=Path("/home/user/.ssh/id_rsa"))
    with pytest.raises(ValueError, match="SSH key not found: ~/.ssh/id_rsa"):
        SshAuthConfig(key_path="~/.ssh/id_rsa")


def test_password_and_key_path_none():
    with pytest.raises(ValueError, match="Either password or key_path must be provided"):
        SshAuthConfig()
