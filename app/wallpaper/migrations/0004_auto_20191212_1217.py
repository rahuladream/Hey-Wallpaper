# Generated by Django 2.2.6 on 2019-12-12 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0003_wallpaper_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallpaper',
            name='tags',
            field=models.ManyToManyField(null=True, to='wallpaper.Tag'),
        ),
        migrations.AlterField(
            model_name='wallpaper',
            name='total_download',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wallpaper',
            name='total_views',
            field=models.IntegerField(default=0),
        ),
    ]
