# Generated by Django 2.2.10 on 2020-03-16 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200316_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='title',
            new_name='titles',
        ),
    ]
