# Generated by Django 4.2.1 on 2023-06-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_product_availabe_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('phone', models.CharField(max_length=264)),
                ('message', models.TextField(max_length=512)),
            ],
        ),
    ]