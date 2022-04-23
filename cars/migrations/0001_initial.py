# Generated by Django 4.0.4 on 2022-04-23 17:36

import cars.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Dr', 'Dr'), ('Rev', 'Rev'), ('Honorable', 'Honorable'), ('Ms', 'Ms'), ('Mrs', 'Mrs'), ('Mr', 'Mr')], max_length=25)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('car_model', models.CharField(max_length=100)),
                ('car_model_year', models.PositiveIntegerField(default=2022, validators=[django.core.validators.MinValueValidator(1900), cars.models.max_value_current_year])),
                ('car_number', models.CharField(max_length=25)),
                ('color', models.CharField(max_length=10)),
                ('car_price', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(100000)])),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]