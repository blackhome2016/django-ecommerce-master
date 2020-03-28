# Generated by Django 2.2.10 on 2020-03-24 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20200324_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='SubCategory_ar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='SubCategory_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category_ar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.category'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.category'),
        ),
    ]