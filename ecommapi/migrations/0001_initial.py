# Generated by Django 4.0.5 on 2022-06-23 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=150)),
                ('initial_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('stock', models.IntegerField()),
                ('image', models.URLField()),
                ('status', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ecommapi.category')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('isbn', models.CharField(max_length=13)),
                ('pages', models.IntegerField()),
                ('initial_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('stock', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.URLField()),
                ('status', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='ecommapi.category')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
