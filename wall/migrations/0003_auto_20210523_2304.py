# Generated by Django 3.2 on 2021-05-23 17:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wall', '0002_auto_20210523_2258'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='PostComment',
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
