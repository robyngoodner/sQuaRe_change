# Generated by Django 4.0.4 on 2022-04-18 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0008_remove_donor_status_donor_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipient',
            name='status',
        ),
        migrations.AddField(
            model_name='recipient',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
