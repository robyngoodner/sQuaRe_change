# Generated by Django 4.0.4 on 2022-04-21 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='bio',
        ),
        migrations.AddField(
            model_name='recipient',
            name='bio',
            field=models.CharField(default='This is a default bio. It tells you a lot about me', max_length=500),
            preserve_default=False,
        ),
    ]
