# Generated by Django 4.2.5 on 2023-09-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formfill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
                ('account_type', models.CharField(max_length=200)),
                ('credit_card', models.BooleanField(default=False)),
                ('debit_card', models.BooleanField(default=False)),
                ('cheque_book', models.BooleanField(default=False)),
            ],
        ),
    ]