# Generated by Django 4.1.7 on 2023-03-03 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.address')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.address')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
                ('total_value', models.FloatField(default=0)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.currency')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
                ('quantityUnit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.quantityunit')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
                ('total_value', models.FloatField(default=0)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.currency')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
                ('quantityUnit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.address')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.vendor')),
            ],
        ),
    ]
