# Generated by Django 4.1 on 2022-08-22 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_remove_team_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='img',
            field=models.ImageField(default='2022.08.22', upload_to='photos'),
            preserve_default=False,
        ),
    ]