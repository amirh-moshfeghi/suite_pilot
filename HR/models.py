from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm
from tinymce.models import HTMLField

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
        verbose_name="وضعیت مدیر",
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


class Company(models.Model):
    """
    Model for company classes
    """

    Company_STATUS = (
        ('فعال', 'فعال'),
        ('غیر فعال', 'غیر فعال'),
    )

    # Fields
    title = models.CharField(
        max_length=35,
        verbose_name="نام شرکت",
    )
    code = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        verbose_name="کد شرکت",
    )
    english_title = models.CharField(
        max_length=35,
        verbose_name="نام انگلیسی شرکت",
    )

    company_status = models.CharField(
        choices=Company_STATUS,
        max_length=15,
        null=True,
        blank=True,
        verbose_name="وضعیت شرکت",
    )

    content = HTMLField(blank=True, null=True)

    # Metadata
    class Meta:
        verbose_name = 'شرکت'
        verbose_name_plural = 'شرکت ها'

    # Methods
    def __str__(self):
        return self.title


class Department(models.Model):
    """
    Model for department classes
    """

    Department_STATUS = (
        ('فعال', 'فعال'),
        ('غیر فعال', 'غیر فعال'),
    )

    Department_TYPE = (
        ('صف', 'صف'),
        ('ستاد', 'ستاد'),
    )

    # Fields
    title = models.CharField(
        max_length=35,
        verbose_name="نام معاونت",
    )
    code = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        verbose_name="کد معاونت",
    )
    english_title = models.CharField(
        max_length=35,
        verbose_name="نام انگلیسی معاونت",
    )

    department_status = models.CharField(
        choices=Department_STATUS,
        max_length=15,
        null=True,
        blank=True,
        verbose_name="وضعیت معاونت",
    )

    department_type = models.CharField(
        choices=Department_TYPE,
        max_length=15,
        null=True,
        blank=True,
        verbose_name="نوع معاونت",
    )

    order = models.IntegerField(
        max_length=35,
        verbose_name="ترتیب معاونت",
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE,blank=True,null=True)

    # Metadata
    class Meta:
        verbose_name = 'معاونت'
        verbose_name_plural = 'معاونت ها'

    # Methods
    def __str__(self):
        return self.title


class OU(models.Model):
    """
    Model for OU classes
    """

    OU_STATUS = (
        ('فعال', 'فعال'),
        ('غیر فعال', 'غیر فعال'),
    )

    # Fields
    title = models.CharField(
        max_length=35,
        verbose_name="نام واحد سازمانی",
    )
    code = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        verbose_name="کد واحد سازمانی",
    )
    english_title = models.CharField(
        max_length=35,
        verbose_name="نام انگلیسی واحد سازمانی",
    )

    ou_status = models.CharField(
        choices=OU_STATUS,
        max_length=15,
        null=True,
        blank=True,
        verbose_name="وضعیت واحد سازمانی",
    )

    order = models.IntegerField(
        max_length=35,
        verbose_name="ترتیب واخد سازمانی",
    )

    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)

    # Metadata
    class Meta:
        verbose_name = 'واحد سازمانی'
        verbose_name_plural = 'واحد های سازمانی'

    # Methods
    def __str__(self):
        return self.title


class Level(models.Model):
    """
    Model for level classes
    """

    Position_STATUS = (
        ('فعال', 'فعال'),
        ('غیر فعال', 'غیر فعال'),
    )


    # Fields
    title = models.CharField(
        max_length=35,
        verbose_name="نام دسته سمت",
    )
    code = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        verbose_name="کد دسته سمت",
    )


    english_title = models.CharField(
        max_length=35,
        verbose_name="نام انگلیسی دسته سمت",
    )

    position_status = models.CharField(
        choices=Position_STATUS,
        max_length=15,
        null=True,
        blank=True,
        verbose_name="وضعیت دسته سمت",
    )

    grade = models.IntegerField(
        max_length=35,
        verbose_name="ترتیب دسته سمت",
    )


    # Metadata
    class Meta:
        verbose_name = 'دسته سمت'
        verbose_name_plural = 'دسته های سمت'

    # Methods
    def __str__(self):
        return self.title


class Position(models.Model):
    """
    Model for position classes
    """

    Position_STATUS = (
        ('فعال', 'فعال'),
        ('غیر فعال', 'غیر فعال'),
    )

    Position_TYPE = (
        ('ساختاری', 'ساختاری'),
        ('غیر ساختاری', 'غیر ساختاری'),
    )

    # Fields
    title = models.CharField(
        max_length=35,
        verbose_name="نام سمت",
    )
    code = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        verbose_name="کد سمت",
    )

    serial = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        verbose_name="سریال سمت",
    )

    english_title = models.CharField(
        max_length=35,
        verbose_name="نام انگلیسی سمت",
    )

    position_status = models.CharField(
        choices=Position_STATUS,
        max_length=15,
        null=True,
        blank=True,
        verbose_name="وضعیت سمت",
    )

    position_type = models.CharField(
        choices=Position_TYPE,
        max_length=15,
        null=True,
        blank=True,
        verbose_name="نوع سمت",
    )

    order = models.IntegerField(
        max_length=35,
        verbose_name="ترتیب سمت",
    )

    ou = models.ForeignKey(OU, on_delete=models.CASCADE, blank=True, null=True)
    report_to = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    deputy = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, blank=True, null=True)

    # Metadata
    class Meta:
        verbose_name = 'سمت'
        verbose_name_plural = 'سمت ها'

    # Methods
    def __str__(self):
        return self.title

