# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0021_auto_20170120_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contestant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Contestant')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Test')),
            ],
        ),
    ]
