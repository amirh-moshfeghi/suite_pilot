# Generated by Django 4.2.1 on 2023-06-06 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0003_alter_company_company_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_status',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1')], max_length=15, null=True, verbose_name='وضعیت شرکت'),
        ),
    ]
