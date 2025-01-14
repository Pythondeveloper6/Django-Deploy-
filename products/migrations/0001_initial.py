# Generated by Django 4.2 on 2024-01-11 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='brands')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Product Name')),
                ('image', models.ImageField(upload_to='products', verbose_name='Image')),
                ('price', models.FloatField(verbose_name='Price')),
                ('subtitle', models.TextField(max_length=500, verbose_name='Subtitle')),
                ('description', models.TextField(max_length=50000, verbose_name='Description')),
                ('sku', models.IntegerField(verbose_name='SKU')),
                ('video', models.URLField(blank=True, null=True, verbose_name='Video')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('flag', models.CharField(choices=[('New', 'New'), ('Sale', 'Sale'), ('Feature', 'Feature')], max_length=10, verbose_name='Flag')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_brand', to='products.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=300)),
                ('rate', models.IntegerField()),
                ('created_at', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_product', to='products.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='review_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='products.product')),
            ],
        ),
    ]
