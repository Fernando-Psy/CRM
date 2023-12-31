# Generated by Django 4.2.4 on 2023-08-18 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('birthDate', models.DateField()),
                ('areaCode', models.CharField(max_length=3)),
                ('phoneNumber', models.CharField(max_length=9)),
                ('country', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
