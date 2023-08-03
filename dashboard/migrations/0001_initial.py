# Generated by Django 4.2.1 on 2023-08-01 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuickLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('title', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'لینک سریع',
                'verbose_name_plural': 'لینک های سریع',
            },
        ),
    ]
