# Generated by Django 4.2 on 2024-02-18 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='mobile_app',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
