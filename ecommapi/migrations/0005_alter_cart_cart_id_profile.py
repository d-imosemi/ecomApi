# Generated by Django 4.0.5 on 2022-06-29 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommapi', '0004_rename_quantity_cart_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('zipcode', models.PositiveBigIntegerField(default=0)),
                ('phonenumber', models.PositiveBigIntegerField(default=0)),
                ('country', models.CharField(choices=[('Nigeria', 'Nigeria')], max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=20)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
