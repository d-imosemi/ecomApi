# Generated by Django 4.0.5 on 2022-07-08 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapi', '0010_alter_category_title_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=20),
        ),
    ]