# Generated by Django 3.2.9 on 2021-12-18 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dig_marketplace', '0004_remove_customuser_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='month_joined',
            field=models.CharField(blank=True, max_length=30, verbose_name='month_joined'),
        ),
    ]
