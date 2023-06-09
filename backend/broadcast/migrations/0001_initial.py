# Generated by Django 4.2 on 2023-06-14 20:36

import broadcast.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BroadCastModel',
            fields=[
                ('broadcast_date', models.CharField(default='2023-06-14', max_length=300)),
                ('broadcasted_audio_title', models.CharField(max_length=250, primary_key=True, serialize=False, unique=True)),
                ('broadcasted_file', models.FileField(upload_to=broadcast.models.broadcast_audio_directories)),
                ('broadcaster', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StackModel',
            fields=[
                ('title', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('broadcast_audios', models.ManyToManyField(to='broadcast.broadcastmodel')),
            ],
        ),
    ]
