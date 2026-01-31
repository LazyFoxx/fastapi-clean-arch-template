from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True, slots=True)
class GetProfileserInput:
    user_id: str


@dataclass(frozen=True, slots=True)
class GetProfileUserOutput:
    first_name: str
    last_name: str
    avatar_url: str
    bio: Optional[str] = None
