from schemas import UserBase, User
from typing import Dict
from typing import List

DATA_BASE: Dict[str, User] = {}


def create_user(user_base: UserBase):
    user_id = len(DATA_BASE) + 1
    user = User(id=user_id, **user_base.dict())
    DATA_BASE[user.username] = user

def get_db() -> List[User]:
    return list(DATA_BASE.values())
