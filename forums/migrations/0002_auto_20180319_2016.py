# Generated by Django 2.0.3 on 2018-03-19 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='board_headimage',
            field=models.ImageField(default='img/normal.jpg', upload_to='img'),
        ),
        migrations.AddField(
            model_name='forumuser',
            name='gender',
            field=models.IntegerField(default=-1),
        ),
    ]
