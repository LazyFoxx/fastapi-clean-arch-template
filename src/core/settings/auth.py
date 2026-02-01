from functools import cached_property
from pydantic_settings import BaseSettings, SettingsConfigDict
from authlib.jose import JsonWebToken

class AuthSettings(BaseSettings):
    jwks_url: str
    issuer: str
    algorithm: str = "RS256"
    jwks_cache_ttl_seconds: int = 3600

    @cached_property
    def json_web_token(self) -> JsonWebToken:
        return JsonWebToken([self.algorithm])

    model_config = SettingsConfigDict(
        env_prefix="AUTH_", case_sensitive=False, extra="ignore"
    )
