from graphene_django import DjangoObjectType

from .models import User, Profile, LoginRecord


class UserType(DjangoObjectType):
    class Meta:
        model = User


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


class LoginRecordType(DjangoObjectType):
    class Meta:
        model = LoginRecord
