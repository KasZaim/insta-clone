# Generated by Django 5.1 on 2024-09-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instadb', '0006_remove_posts_description_posts_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
