from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    db_uri: PostgresDsn

    # Making this hashable allows for lru_cache use
    def __hash__(self) -> int:
        return hash(self.db_uri)
