import graphene
import graphql_jwt

from .mutations import Register, SendSmsCode
from .types import UserType


class Query(graphene.ObjectType):
    me = graphene.Field(UserType)

    def resolve_me(self, info):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception('Authentication Failure: Your must be signed in')
        return user


class Mutation(graphene.ObjectType):
    register = Register.Field()
    send_sms_code = SendSmsCode.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
