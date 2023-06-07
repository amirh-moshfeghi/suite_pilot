from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver

from extensions.utils import jalali_converter


# Create your models here.
class User(AbstractUser):
    username = models.TextField(unique=True, verbose_name='نام کاربری')
    special_user = models.DateTimeField(default=timezone.now, verbose_name="کاربر ویژه تا")

    def __str__(self):
        return self.email

    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False

    is_special_user.boolean = True
    is_special_user.short_description = "وضعیت کاربر "


class AuditEntry(models.Model):
    action = models.CharField(max_length=64)
    ip = models.GenericIPAddressField(null=True)
    username = models.CharField(max_length=256, null=True)
    time = models.DateTimeField(auto_now_add=True, verbose_name="زمان ورود")

    class Meta:

        verbose_name = 'لاگ ورود به سیستم'
        verbose_name_plural = 'لاگ های ورود به سیستم'

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)

    def jpublish(self):
        return jalali_converter(self.time)



    jpublish.short_description = "زمان ورود به سیستم"


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    now = timezone.now()
    AuditEntry.objects.create(action='user_logged_in', ip=ip, username=user.username, time=now)


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    if user:
        ip = request.META.get('REMOTE_ADDR')
        now = timezone.now()
        AuditEntry.objects.create(action='user_logged_out', ip=ip, username=user.username, time=now)
    else:
        ip = request.META.get('REMOTE_ADDR')
        now = timezone.now()
        AuditEntry.objects.create(action='user_logged_out', ip=ip, username=request.user.username, time=now)


@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, **kwargs):
    now = timezone.now()
    AuditEntry.objects.create(action='user_login_failed', username=credentials.get('username', None), time=now)