from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    user: str
    password: str
    database: str
    host: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    model_config = SettingsConfigDict(env_file="~/.env")


settings = Settings()

# print(settings.model_dump())
