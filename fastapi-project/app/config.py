from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_PATH: str
    MODEL_INFO_PATH: str
    API_VERSION: str = "v1"

    class Config:
        env_file = ".env"

settings = Settings()
