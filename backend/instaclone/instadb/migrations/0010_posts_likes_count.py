# Generated by Django 5.1 on 2024-09-18 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instadb', '0009_posts_liked_by_me'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
    ]
