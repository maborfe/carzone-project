# Generated by Django 4.1 on 2022-08-22 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_picture_team_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='img',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]