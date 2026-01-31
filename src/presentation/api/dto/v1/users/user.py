from pydantic import BaseModel, Field
from typing import Optional


class UserProfileResponse(BaseModel):
    first_name: str
    last_name: str
    avatar_url: str
    bio: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "examples":
                {
                    "first_name": "Дмитрий",
                    "last_name": "Черноморов",
                    "avatar_url": "https//sdfd",
                    "bio": None,
                },

        }
    }