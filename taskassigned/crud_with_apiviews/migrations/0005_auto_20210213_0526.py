# Generated by Django 3.1.6 on 2021-02-13 05:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crud_with_apiviews', '0004_auto_20210212_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='DOB',
            field=models.DateField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
