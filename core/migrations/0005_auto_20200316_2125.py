# Generated by Django 2.2.10 on 2020-03-16 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200316_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='title',
        ),
        migrations.AddField(
            model_name='item',
            name='title',
            field=models.ManyToManyField(related_name='titles', to='core.category'),
        ),
    ]