# Generated by Django 4.1.7 on 2023-03-05 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='product',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='quantityUnit',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='product',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='quantityUnit',
        ),
        migrations.CreateModel(
            name='SaleLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
                ('total_value', models.FloatField(default=0)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.currency')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
                ('quantityUnit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.quantityunit')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
                ('total_value', models.FloatField(default=0)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.currency')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
                ('quantityUnit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.address')),
            ],
        ),
    ]
