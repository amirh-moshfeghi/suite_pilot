from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from Accounts.models import User
from extensions.utils import jalali_converter


# Create your models here.
class FormLetters(models.Model):
    """
    Model for main form letters
    """

    # Fields
    id = models.BigIntegerField(
        unique=True,
        primary_key=True,
    )
    title = models.CharField(
        max_length=256,
    )

    text = RichTextUploadingField(
        max_length=1000,
        verbose_name='عنوان نامه',
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='زمان ارسال نامه'
    )
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)

    # Metadata
    class Meta:
        verbose_name = "نامه"
        verbose_name_plural = 'نامه ها'

    # Methods
    def jpublish(self):
        return jalali_converter(self.created)

    jpublish.short_description = "زمان ارسال نامه"

    def __str__(self):
        return self.title
