from pathlib import Path
from typing import Optional, Self

from pydantic import BaseModel, field_validator, model_validator


class Config(BaseModel):
    """
    SSH Authentication configuration that accepts either password or key_filename
    """
    password: Optional[str] = None
    key_filename: Optional[str] = None

    @field_validator('key_filename')
    def validate_key_filename(cls, path: Optional[str]) -> Optional[str]:
        if path and not Path(path).expanduser().exists():
            raise ValueError(f"SSH key not found: {path}")
        return path

    def __str__(self) -> str:
        auth_type = "key" if self.key_filename else "password"
        return f"AuthConfig(type={auth_type})"

    @model_validator(mode='before')
    def check_auth_method(cls, values):
        """Ensure only one authentication method is provided"""
        password, key_filename = values.get('password'), values.get('key_filename')
        if password and key_filename:
            raise ValueError("Cannot specify both password and key_filename")
        return values

    @model_validator(mode='after')
    def check_auth_exists(self, values) -> Self:
        """Ensure at least one authentication method is provided"""
        if not self.password and not self.key_filename:
            raise ValueError("Either password or key_filename must be provided")
        return self
