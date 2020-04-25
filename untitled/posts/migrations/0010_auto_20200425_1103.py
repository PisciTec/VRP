# Generated by Django 3.0.4 on 2020-04-25 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_posts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='posx',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='posts',
            name='posy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='posts',
            name='posz',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.FileField(default='null', upload_to='images'),
        ),
    ]