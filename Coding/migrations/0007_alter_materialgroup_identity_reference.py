# Generated by Django 4.2.1 on 2023-08-17 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Coding', '0006_alter_materialgroup_identity_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialgroup',
            name='identity_reference',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Coding.materialgroup'),
        ),
    ]
