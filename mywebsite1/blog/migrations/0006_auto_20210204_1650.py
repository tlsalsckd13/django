# Generated by Django 3.1.5 on 2021-02-04 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210204_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='music_no',
        ),
        migrations.AddField(
            model_name='playlist',
            name='music_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='playlist_music_no', to='blog.music'),
        ),
    ]
