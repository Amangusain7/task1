# Generated by Django 3.1.6 on 2021-02-12 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_with_apiviews', '0002_auto_20210212_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='email_id',
            field=models.EmailField(default=None, max_length=70),
        ),
    ]
