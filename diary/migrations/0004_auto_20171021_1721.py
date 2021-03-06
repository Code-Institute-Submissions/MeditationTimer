# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_diaryentry_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diaryentry',
            old_name='content',
            new_name='insights',
        ),
        migrations.RemoveField(
            model_name='diaryentry',
            name='intention',
        ),
        migrations.AddField(
            model_name='diaryentry',
            name='mind',
            field=models.CharField(choices=[('very bad', 'very bad'), ('bd', 'bad'), ('OK', 'OK'), ('good', 'good'), ('very good', 'very good')], default='OK', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='diaryentry',
            name='body',
            field=models.CharField(choices=[('very bad', 'very bad'), ('bd', 'bad'), ('OK', 'OK'), ('good', 'good'), ('very good', 'very good')], default='OK', max_length=200, null=True),
        ),
    ]
