from django.db import models
from Accounts.models import User
from extensions.utils import jalali_converter


# Create your models here.
class Notification(models.Model):
    """
    Model for notifications
    """

    # Fields

    Notification_STATUS = (
        ('خوانده شده', 'خوانده شده'),
        ('خوانده نشده', 'خوانده نشده'),
    )

    title = models.CharField(
        max_length=35,
        verbose_name="تیتر پیام",
    )
    description = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        verbose_name="متن پیام",
    )

    notif_status = models.CharField(
        choices=Notification_STATUS,
        max_length=15,
        null=True,
        blank=True,
        verbose_name="وضعیت پیام",
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    notifications_date = models.DateTimeField(auto_now_add=True,verbose_name="زمان پیام")

    def jpublish(self):
        return jalali_converter(self.notifications_date)

    jpublish.short_description = "زمان انتشار پیام"

    def __str__(self):
        return self.title


    # Metadata
    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'





