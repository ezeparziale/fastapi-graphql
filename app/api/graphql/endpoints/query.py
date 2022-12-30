from datetime import datetime
from typing import List

import strawberry
from strawberry.fastapi import GraphQLRouter

from app.api.graphql.deps import IsAuthenticated
from app.db.database import get_db
from app.models import User
from app.schemas import UserQ


@strawberry.type
class Query:
    @strawberry.field(
        description="Get one user info", permission_classes=[IsAuthenticated]
    )
    def GetUser(id: int) -> UserQ:
        db = next(get_db())
        return db.query(User).filter(User.id == id).first()

    @strawberry.field(
        description="Get all users info", permission_classes=[IsAuthenticated]
    )
    def GetUsers(self) -> List[UserQ]:
        db = next(get_db())
        return db.query(User).all()
