# Generated by Django 4.1.3 on 2022-12-22 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='handle',
        ),
    ]
