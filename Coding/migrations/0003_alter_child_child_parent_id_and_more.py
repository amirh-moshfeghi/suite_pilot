# Generated by Django 4.2.1 on 2023-08-17 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Coding', '0002_alter_materialgroup_identity_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='child_parent_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='materialgroup',
            name='identity_reference',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Coding.materialgroup'),
        ),
    ]
