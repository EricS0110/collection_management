from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings, SecretStr


BASE_DIR = Path(__file__).parent.resolve()


class Settings(BaseSettings):
    """https://pydantic-docs.helpmanual.io/usage/settings"""

    # MongoDB Connection credentials
    mongo_username: str
    mongo_password: SecretStr
    mongo_cluster: str
    mongo_database: str


def get_settings():
    load_dotenv(BASE_DIR / "configuration" / "secrets.env")
    settings = Settings()

    return settings
