import random

import graphene
from django.core.cache import cache
from django.utils.timezone import now
from graphene_django.forms.mutation import DjangoFormMutation
from graphql_jwt.refresh_token.shortcuts import create_refresh_token
from graphql_jwt.shortcuts import get_token

from const import const
from .forms import EmailForm, RegisterForm
from .models import User, Profile
from .types import UserType


class Register(DjangoFormMutation):
    """ 执行注册 """
    user = graphene.Field(UserType)
    token = graphene.String()
    refresh_token = graphene.String()

    class Meta:
        form_class = RegisterForm

    @classmethod
    def perform_mutate(cls, form, info):
        version = info.context.headers.get('version', '')
        source = info.context.headers.get('source', '')
        ip = info.context.META.get('REMOTE_ADDR', '')
        # 1. 创建基础信息表
        user = User.objects.create_user(
            username=form.cleaned_data.get("username"),
            password=form.cleaned_data.get("password"),
            email=form.cleaned_data.get("email"),
            is_email_valid=True
        )
        token = get_token(user)
        refresh_token = create_refresh_token(user)
        # 3. 记录登录日志
        user.last_login = now()
        user.save()
        user.add_login_record(ip=ip, source=source, version=version)

        return cls(errors=[], user=user, token=token,
                   refresh_token=refresh_token, **form.cleaned_data)


class SendSmsCode(DjangoFormMutation):
    """ 发送邮箱验证码 """
    sms_code = graphene.Int()
    timeout = graphene.Int()

    class Meta:
        form_class = EmailForm

    @classmethod
    def perform_mutate(cls, form, info):
        sms_code = random.randint(100000, 999999)
        # TODO 调用发送验证码的短信接口
        # redis中的key
        key = '{}{}'.format(const.REGISTER_MSM_CODE_KEY, form.cleaned_data.get("email"))
        # 将验证码存入redis
        timeout = 5 * 60
        cache.set(key, sms_code, timeout=timeout)
        return cls(errors=[], sms_code=sms_code, timeout=timeout, **form.cleaned_data)
