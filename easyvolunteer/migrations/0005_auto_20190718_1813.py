# Generated by Django 2.1.5 on 2019-07-18 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easyvolunteer', '0004_auto_20190717_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organ',
            name='area',
        ),
        migrations.RemoveField(
            model_name='organ',
            name='phoneNum',
        ),
    ]
