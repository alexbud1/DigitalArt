# Generated by Django 3.2.9 on 2021-12-27 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dig_marketplace', '0009_alter_customuser_email_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email_hash',
            field=models.CharField(blank=True, max_length=250, unique=True, verbose_name='email_hash'),
        ),
    ]
