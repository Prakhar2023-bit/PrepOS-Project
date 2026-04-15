from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "PrepOS API"
    DATABASE_URL: str
    GROQ_API_KEY: str

    class Config:
        env_file = ".env"

# Create a global settings object to use throughout the app
settings = Settings()