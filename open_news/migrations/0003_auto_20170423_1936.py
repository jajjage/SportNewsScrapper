# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 19:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('open_news', '0002_article_date_of_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='date_of_post',
            new_name='date',
        ),
    ]
