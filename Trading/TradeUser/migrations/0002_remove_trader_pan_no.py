# Generated by Django 4.0.4 on 2022-05-29 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TradeUser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trader',
            name='pan_no',
        ),
    ]
