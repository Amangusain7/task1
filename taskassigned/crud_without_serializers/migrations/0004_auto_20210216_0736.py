# Generated by Django 3.1.6 on 2021-02-16 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_without_serializers', '0003_auto_20210216_0734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wwe',
            name='P_name',
        ),
        migrations.AddField(
            model_name='wwe',
            name='p_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]