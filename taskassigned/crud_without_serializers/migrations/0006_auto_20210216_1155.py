# Generated by Django 3.1.6 on 2021-02-16 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_without_serializers', '0005_auto_20210216_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wwe',
            name='p_lock',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
