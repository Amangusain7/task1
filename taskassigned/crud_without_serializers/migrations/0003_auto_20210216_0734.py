# Generated by Django 3.1.6 on 2021-02-16 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_without_serializers', '0002_auto_20210216_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wwe',
            name='P_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
