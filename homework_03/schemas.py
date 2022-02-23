from pydantic import BaseModel, validator, Field
from datetime import date, datetime


class UserIn(BaseModel):
    username: str
    password: str

    @validator("username")
    def validate_username(cls, name: str):

        if len(name) < 3:
            raise ValueError("name is too short")

        if name[0].isdigit():
            raise ValueError("first symbol cannot be digit")

        return name

    @validator("password")
    def validate_password(cls, pswd: str):

        if len(pswd) < 5:
            raise ValueError("password is too short")

        return pswd


class UserBase(UserIn):
    create_at: date = Field(default_factory=datetime.now)


class UserOut(UserBase):
    pass


class User(UserBase):
    id: int
