import strawberry
from fastapi import APIRouter
from strawberry.fastapi import GraphQLRouter

from app.api.graphql.endpoints.mutation import Mutation
from app.api.graphql.endpoints.query import Query

api_router_graphql = APIRouter()


schema = strawberry.Schema(Query, Mutation)

graphql_app = GraphQLRouter(schema)


api_router_graphql.include_router(graphql_app, prefix="/graphql", tags=["graphQL"])
