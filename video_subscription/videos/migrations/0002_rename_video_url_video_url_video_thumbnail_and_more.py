# Generated by Django 5.1.1 on 2024-10-06 12:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='video_url',
            new_name='url',
        ),
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(default='http://example.com/default_thumbnail.jpg', upload_to='thumbnails/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='upload_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]