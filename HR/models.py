from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm

class Headquarter(models.Model):
    """
    Model for School grads
    """

    # Fields
    name = models.CharField(
        max_length=30,
        verbose_name="نام ستاد",
    )

    # Metadata
    class Meta:
        verbose_name = 'نام ستاد'
        verbose_name_plural = 'نام ستاد ها'

    # Methods
    def __str__(self):
        return self.name


# Major Section
class Queue(models.Model):
    """
    Model for School major
    """

    # Fields
    name = models.CharField(
        max_length=30,
        verbose_name="نام صف",
    )

    # Metadata
    class Meta:
        verbose_name = 'صف'
        verbose_name_plural = 'صف ها'

    # Methods
    def __str__(self):
        return self.name


class Manager(models.Model):
    """
    Model for administrator classes
    """

    Manager_STATUS = (
        ('فعال', 'فعال'),
        ('غیر فعال', 'غیر فعال'),
    )

    # Fields
    persian_name = models.CharField(
        max_length=35,
        verbose_name="نام مدیریت",
    )
    code = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        verbose_name="کد مدیریت",
    )
    english_name = models.CharField(
        max_length=35,
        verbose_name="نام انگلیسی مدیریت",
    )

    order = models.IntegerField(
        max_length=35,
        verbose_name="ترتیب",
    )

    manager_status = models.CharField(
        choices=Manager_STATUS,
        max_length=15,
        null=True,
        blank=True,
        verbose_name="وضعیت حضور و غیاب",
    )

    queue = models.ForeignKey(
        Queue,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="queue",
        verbose_name="صف",
    )
    headquarter = models.ForeignKey(
        Headquarter,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="headquarter",
        verbose_name="ستاد",
    )

    # Metadata
    class Meta:
        verbose_name = 'مدیریت'
        verbose_name_plural = 'مدیران'

    # Methods
    def __str__(self):
        return self.persian_name

