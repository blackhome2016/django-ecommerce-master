# Generated by Django 2.2.10 on 2020-03-16 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200316_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Sub_category',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='title',
        ),
    ]