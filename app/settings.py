from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_port: str | int
    postgres_host: str

    class Config:
        env_file = '.env'


settings = Settings()
