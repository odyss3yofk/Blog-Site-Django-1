# Generated by Django 5.1.4 on 2025-01-31 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_image_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image_name',
            new_name='image',
        ),
    ]
