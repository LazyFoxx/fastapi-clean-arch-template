from pydantic_settings import BaseSettings, SettingsConfigDict


class AuthSettings(BaseSettings):
    jwks_url: str
    issure: str
    audience: str
    algorithm: str = "RS256"
    jwks_cache_ttl_seconds: int = 3600

    model_config = SettingsConfigDict(
        env_prefix="AUTH_", case_sensitive=False, extra="ignore"
    )
