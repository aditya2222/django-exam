# Generated by Django 2.2 on 2019-04-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionpaper',
            name='answer1Boolean',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='questionpaper',
            name='answer2Boolean',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
