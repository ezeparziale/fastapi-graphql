from datetime import datetime
from typing import List

import strawberry
from strawberry.fastapi import GraphQLRouter

from app.db.database import get_db
from app.models import User
from app.schemas import UserCreateQ, UserQ


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def CreateUser(self, email: str, password: str) -> UserQ:
        new_user = UserCreateQ(email=email, password=password)
        new_user.to_pydantic()
        db = next(get_db())
        new_user = User(**new_user.__dict__)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
