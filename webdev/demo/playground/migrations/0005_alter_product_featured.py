# Generated by Django 4.0.5 on 2022-07-05 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0004_alter_product_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]