# Generated by Django 5.1 on 2024-09-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instadb', '0011_rename_likes_count_posts_total_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='total_likes',
            field=models.IntegerField(),
        ),
    ]
