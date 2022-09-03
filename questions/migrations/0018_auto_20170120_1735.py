# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0017_auto_20170120_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='question',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]