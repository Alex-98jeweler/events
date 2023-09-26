import dataclasses
import datetime
import jwt
from typing import TYPE_CHECKING
from django.conf import settings

from .models import User


@dataclasses.dataclass
class UserDataClass:
    first_name: str
    last_name: str
    username: str
    password: str = None
    id: int = None
    
    @classmethod
    def from_instance(cls, user: "User") -> "UserDataClass":
        return cls(
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            id=user.id
        )
        
def create_user(user_dc: UserDataClass) -> UserDataClass:
    obj = User(
        first_name=user_dc.first_name,
        last_name=user_dc.last_name,
        username=user_dc.username
    )
    if user_dc.password is not None:
        obj.set_password(user_dc.password)
    obj.save()
    return UserDataClass.from_instance(obj)

def user_username_selector(username: str) -> User:
    user = User.objects.get(username=username)
    return user

def create_token(user_id: int) -> str:
    payload = dict(
        id=user_id,
        exp=datetime.datetime.utcnow() + datetime.timedelta(days=30),
        iat=datetime.datetime.utcnow()
    )
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
    return token
    