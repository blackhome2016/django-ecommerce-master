# Generated by Django 2.2.10 on 2020-03-16 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200316_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='title',
        ),
        migrations.RemoveField(
            model_name='item',
            name='titles',
        ),
        migrations.AddField(
            model_name='item',
            name='title',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]
