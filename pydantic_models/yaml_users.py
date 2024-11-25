import os
from datetime import datetime
from typing import List

import yaml
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: datetime | None


class UserConfig(BaseModel):
    users: List[User]


def load_users(yaml_path: str) -> List[User]:
    with open(yaml_path, 'r') as file:
        config_data = yaml.safe_load(file)
        user_config = UserConfig(users=config_data['users'])
        return user_config.users


if __name__ == "__main__":
    example_yaml = """
    users:
      - id: 1
        name: Alice Smith
        signup_ts: 2024-01-01T10:00:00
      - id: 2
        name: Bob Jones
        signup_ts: 1732525901
      - id: 3
        name: Charlie Brown
        signup_ts: null
    """
    with open('users.yaml', 'w') as f:
        f.write(example_yaml)
    users = load_users('users.yaml')
    for user in users:
        print(f"User {user.id}: {user.name} (Signed up: {user.signup_ts})")
    os.remove('users.yaml')
