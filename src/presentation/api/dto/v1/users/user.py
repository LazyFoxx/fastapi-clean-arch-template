from typing import Optional

from pydantic import BaseModel


class UserProfileResponse(BaseModel):
    first_name: str
    last_name: str
    avatar_url: str
    bio: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "avatar_url": "https://example.com/avatar.png",
                    "first_name": "Иван",
                    "last_name": "Черноморов",
                }
            ]
        }
    }
