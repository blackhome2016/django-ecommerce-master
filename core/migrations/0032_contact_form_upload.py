# Generated by Django 2.2.10 on 2020-03-24 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_title_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_form',
            name='Upload',
            field=models.FileField(default=True, upload_to=''),
            preserve_default=False,
        ),
    ]
