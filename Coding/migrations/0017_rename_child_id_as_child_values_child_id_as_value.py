# Generated by Django 4.2.1 on 2023-08-14 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Coding', '0016_alter_values_child_id_as_child'),
    ]

    operations = [
        migrations.RenameField(
            model_name='values',
            old_name='child_id_as_child',
            new_name='child_id_as_value',
        ),
    ]
