# Generated by Django 4.2.1 on 2023-08-14 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Coding', '0002_child_child_id_as_parent_values_child_id_as_child'),
    ]

    operations = [
        migrations.AlterField(
            model_name='values',
            name='child_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_related', to='Coding.child'),
        ),
    ]
