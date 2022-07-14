# Generated by Django 4.0.5 on 2022-07-14 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapi', '0003_alter_address_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart_product', to='ecommapi.product'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=20),
        ),
    ]
