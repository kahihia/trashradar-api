# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-21 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0004_complaints_with_events_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='current_state',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Clean')], default=1),
        ),
    ]