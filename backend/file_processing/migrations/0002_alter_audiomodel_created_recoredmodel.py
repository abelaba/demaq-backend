# Generated by Django 4.2 on 2023-06-11 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import file_processing.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('file_processing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiomodel',
            name='created',
            field=models.CharField(default='2023-06-12', max_length=300),
        ),
        migrations.CreateModel(
            name='RecoredModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('descr', models.CharField(max_length=250)),
                ('audio_file', models.FileField(upload_to=file_processing.models.upload_audio_directory_to)),
                ('created', models.CharField(default='2023-06-12', max_length=300)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
