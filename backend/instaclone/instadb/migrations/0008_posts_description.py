# Generated by Django 5.1 on 2024-09-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instadb', '0007_alter_posts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='description',
            field=models.CharField(default='', max_length=50),
        ),
    ]
