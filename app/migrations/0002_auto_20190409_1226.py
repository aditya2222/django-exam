# Generated by Django 2.2 on 2019-04-09 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjects',
            old_name='quesionPaper',
            new_name='questionPaper',
        ),
    ]
