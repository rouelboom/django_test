# Generated by Django 2.2.9 on 2021-01-10 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210110_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]