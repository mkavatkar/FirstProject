# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160830124855 on 2016-09-01 15:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pub_Date',
            new_name='pub_date',
        ),
    ]