# Generated by Django 4.0.5 on 2022-07-05 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapi', '0009_alter_cart_quantity_alter_product_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20),
        ),
    ]