from typing import Optional

from pydantic import BaseModel


class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            'examples': {
                "username": "johndoe",
                "email": "user@app.com",
                "password": "password",
                "is_staff": False,
                "is_active": True
            }
        }
