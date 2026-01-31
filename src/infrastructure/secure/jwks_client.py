import time
import requests
from jose import jwk
from typing import Dict
from src.core.settings import AuthSettings


class JWKSClient:
    def __init__(self, settings: AuthSettings):
        self._jwks_url = settings.jwks_url
        self._cache_ttl = settings.jwks_cache_ttl_seconds
        self._cached_at: float | None = None
        self._keys: Dict[str, str] = {}

    def get_key(self, kid: str) -> str:
        if self._is_cache_expired():
            self._refresh()

        try:
            return self._keys[kid]
        except KeyError:
            self._refresh()
            return self._keys[kid]

    def _is_cache_expired(self) -> bool:
        if self._cached_at is None:
            return True
        return (time.time() - self._cached_at) > self._cache_ttl

    def _refresh(self) -> None:
        jwks = requests.get(self._jwks_url, timeout=3).json()
        self._keys = {
            key["kid"]: jwk.construct(key).to_pem().decode()
            for key in jwks["keys"]
        }
        self._cached_at = time.time()
