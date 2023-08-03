from django.db import models


class QuickLinks(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length= 200,null=True)

    class Meta:
        verbose_name = 'لینک سریع'
        verbose_name_plural = 'لینک های سریع'

    def __str__(self):
        return self.title


class SubMenu(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length= 200,null=True)

    class Meta:
        verbose_name = 'اپ فرعی'
        verbose_name_plural = 'اپ های فرعی'

    def __str__(self):
        return self.title
