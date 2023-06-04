from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


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