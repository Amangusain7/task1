# Generated by Django 3.1.6 on 2021-02-12 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userlogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(blank=True, default=None, max_length=100)),
                ('l_name', models.CharField(blank=True, default=None, max_length=100)),
                ('DOB', models.IntegerField(default=None, null=True)),
                ('gender', models.CharField(blank=True, max_length=100)),
                ('email_id', models.EmailField(default=None, max_length=70, unique=True)),
                ('phone_no', models.IntegerField(default=None, null=True)),
                ('password', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
