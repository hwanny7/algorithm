# Generated by Django 3.1.7 on 2022-10-06 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('either', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=100),
        ),
    ]
