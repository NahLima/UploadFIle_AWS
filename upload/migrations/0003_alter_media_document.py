# Generated by Django 4.1.2 on 2022-10-21 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_media_alt_media_height_media_width'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='document',
            field=models.ImageField(upload_to='media/cozinhas/'),
        ),
    ]
