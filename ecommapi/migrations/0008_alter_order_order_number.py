# Generated by Django 4.0.5 on 2022-07-14 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapi', '0007_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
