# Generated by Django 2.2 on 2019-04-09 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190409_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='questionPaper',
        ),
    ]