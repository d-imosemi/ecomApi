# Generated by Django 4.0.5 on 2022-07-14 23:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapi', '0008_alter_order_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
    ]
