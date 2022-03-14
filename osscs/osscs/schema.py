import graphene

import accounts.schema
import app.schema


class Query(accounts.schema.Query, app.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(accounts.schema.Mutation, graphene.ObjectType, ):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
