# Generated by Django 5.1.6 on 2025-02-27 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AccountApp', '0002_user_avatarurl'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
