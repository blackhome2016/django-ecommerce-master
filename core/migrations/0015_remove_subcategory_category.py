# Generated by Django 2.2.10 on 2020-03-17 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_subcategory_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
    ]
