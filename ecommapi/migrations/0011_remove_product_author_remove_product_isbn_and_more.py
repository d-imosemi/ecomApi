# Generated by Django 4.0.5 on 2022-07-26 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapi', '0010_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
        migrations.RemoveField(
            model_name='product',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pages',
        ),
    ]
