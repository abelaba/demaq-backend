# Generated by Django 4.2 on 2023-06-12 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0002_newusers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewUsers',
            new_name='NewUsersLog',
        ),
    ]