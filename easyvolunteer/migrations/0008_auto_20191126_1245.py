# Generated by Django 2.2.3 on 2019-11-26 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easyvolunteer', '0007_auto_20190718_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='이메일'),
        ),
    ]