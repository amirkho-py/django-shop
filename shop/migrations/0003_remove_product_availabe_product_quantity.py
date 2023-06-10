# Generated by Django 4.2.1 on 2023-05-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_brand_category_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='availabe',
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]