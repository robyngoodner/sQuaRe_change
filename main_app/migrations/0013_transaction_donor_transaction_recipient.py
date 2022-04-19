# Generated by Django 4.0.4 on 2022-04-19 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_transaction_accounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='donor',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='recipient',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]