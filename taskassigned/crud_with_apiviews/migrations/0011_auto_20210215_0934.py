# Generated by Django 3.1.6 on 2021-02-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_with_apiviews', '0010_auto_20210213_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='f_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
