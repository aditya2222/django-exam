# Generated by Django 2.2 on 2019-04-06 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190406_1213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionpaper',
            old_name='question1Text',
            new_name='option3text',
        ),
        migrations.AddField(
            model_name='questionpaper',
            name='option4text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='questionpaper',
            name='questionText',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]