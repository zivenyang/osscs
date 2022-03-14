from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    """ 用户模型 """
    is_email_valid = models.BooleanField('邮箱是否已经验证', default=False)
    email = models.EmailField('email address', unique=True)

    class Meta:
        db_table = 'account_user'

    def add_login_record(self, **kwargs):
        """ 保存登录历史 """
        self.login_records.create(**kwargs)


class Profile(models.Model):
    """ 用户详细信息 """
    # 年龄
    # 真实姓名
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField('用户头像', upload_to='avatar/%Y%m', null=True, blank=True)
    nickname = models.CharField('昵称', max_length=32, default='小可爱')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        db_table = 'accounts_user_profile'

    @property
    def avatar_url(self):
        return self.avatar.url if self.avatar else ''


class LoginRecord(models.Model):
    """ 用户登录日志 """
    # 关联用户
    # 登录账号
    # 登录的时间
    # ip
    # 登录的来源
    # 登录的客户端版本号
    user = models.ForeignKey(User, related_name='login_records', on_delete=models.CASCADE)
    ip = models.CharField('IP', max_length=32)
    address = models.CharField('地址', max_length=32, null=True, blank=True)
    source = models.CharField('登录的来源', max_length=16, null=True)
    version = models.CharField('登录的版本', max_length=16, null=True)

    created_at = models.DateTimeField('登录时间', auto_now_add=True)

    class Meta:
        db_table = 'accounts_login_record'


class ApiKey(models.Model):
    """ 用户API KEY存储 """
    API_KEY_TYPE_CHOICES = (
        (1, 'github_api'),
        (0, 'libraries_io_api'),
    )
    user = models.ForeignKey(User, related_name='api_key', on_delete=models.CASCADE)
    type = models.SmallIntegerField('api_key类型', choices=API_KEY_TYPE_CHOICES)
    token = models.CharField('密钥', max_length=256)

    class Meta:
        db_table = 'accounts_user_api_key'


# 监听User模型创建
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, nickname=instance.username)


# 监听User模型更新
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
