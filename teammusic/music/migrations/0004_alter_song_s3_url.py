# Generated by Django 5.1.1 on 2024-11-02 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_album_s3_alblumurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='s3_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]