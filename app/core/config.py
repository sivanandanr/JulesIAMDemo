from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Mini-IAM"
    DATABASE_URL: str = "sqlite:///./mini_iam.db"

    class Config:
        case_sensitive = True

settings = Settings()
