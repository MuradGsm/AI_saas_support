from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    
    POSTGRES_HOST: str
    POSTGRES_PORT: int =5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    # DB
    AUTH_DB_NAME: str


    REDIS_URL: str

    # JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.AUTH_DB_NAME}"
    
    @property
    def ALEMBIC_DATABASE_URL(self) -> str:
        return f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.AUTH_DB_NAME}"

    model_config = SettingsConfigDict(
        env_file="../.env",
        extra="ignore",
    )

settings = Settings()

