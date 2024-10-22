# Generated by Django 4.2 on 2024-03-10 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='address',
            field=models.TextField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='type',
            field=models.CharField(choices=[('Home', 'Home'), ('Office', 'Office'), ('Bussines', 'Bussines'), ('Other', 'Other')], default='Home', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
