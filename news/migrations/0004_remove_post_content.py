# Generated by Django 3.1.4 on 2021-01-03 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
    ]
