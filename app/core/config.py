from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # goes up to fastapi-crud-jwt/

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = BASE_DIR / ".env"

settings = Settings()
print("✅ Loaded DB URL:", settings.DATABASE_URL)  # temporary debug line