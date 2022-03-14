import re

from django import forms
from django.core.cache import cache

from accounts.models import User
from const import const


class RegisterForm(forms.Form):
    """ 用户注册 """
    username = forms.CharField(label='用户名', max_length=16, required=True, error_messages={
        'required': '请输入用户名'
    })
    password = forms.CharField(label='密码', max_length=128, required=True, error_messages={
        'required': '请输入密码'
    })
    check_password = forms.CharField(label='确认密码', max_length=128, required=True, error_messages={
        'required': '请确认密码'
    })
    email = forms.EmailField(label='邮箱', max_length=254, required=True, error_messages={
        'required': '请输入邮箱'
    })
    sms_code = forms.IntegerField(label='验证码', required=True, error_messages={
        'required': '请输入验证码'
    })

    def clean_username(self):
        """ 验证用户名 hook 钩子函数 """
        username = self.cleaned_data['username']
        pattern = r'^[a-z0-9_-]{6,16}$'
        if not re.search(pattern, username):
            raise forms.ValidationError('用户名%s输入不正确,只能包含小写字母、数字、中划线和下划线，长度为6-16个字符',
                                        code='invalid_username',
                                        params=(username,))
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已经被使用')
        return username

    def clean_password(self):
        """ 昵称验证 """
        password = self.cleaned_data['password']
        pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9~!@#$%^&*]{8,16}$'
        if not re.search(pattern, password):
            raise forms.ValidationError('密码格式不正确，必须包含大小写字母和数字的组合，可以使用特殊字符(~!@#$\\%^&*)，长度在8-16之间',
                                        code='invalid_password')
        return password

    def clean(self):
        data = super().clean()
        if self.errors:
            return
        # 校验两次密码输入相同
        password = self.cleaned_data.get('password', None)
        check_password = self.cleaned_data.get('check_password', None)
        if password != check_password:
            raise forms.ValidationError('两次输入的密码不同',
                                        code='invalid_check_password')

        # 校验验证码
        email = self.cleaned_data.get('email', None)
        sms_code = self.cleaned_data.get('sms_code', None)
        # redis 中的验证码key
        key = '{}{}'.format(const.REGISTER_MSM_CODE_KEY, email)
        code = cache.get(key)
        # code 已失效
        if code is None:
            raise forms.ValidationError('验证码已经失效')
        if code != sms_code:
            raise forms.ValidationError('验证码输入不正确')
        return data


class EmailForm(forms.Form):
    """ 发送验证码的表单 """
    email = forms.EmailField(label='邮箱', required=True, error_messages={
        'required': '请输入邮箱'
    })
