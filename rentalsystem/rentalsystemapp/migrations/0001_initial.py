# Generated by Django 4.2 on 2024-02-06 02:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import rentalsystemapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=100)),
                ('vechile_type', models.CharField(choices=[('car', 'Car'), ('bike', 'Bike'), ('truck', 'Truck')])),
                ('picture', models.ImageField(upload_to='')),
                ('lincense', models.ImageField(upload_to='')),
                ('verification_status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10)),
            ],
            options={
                'db_table': 'Driver',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_id', models.CharField(default=rentalsystemapp.models.uuid_generate, max_length=32, unique=True)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('picture', models.ImageField(null=True, upload_to='')),
                ('mobile_number', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(db_column='created_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(db_column='updated_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
    ]
