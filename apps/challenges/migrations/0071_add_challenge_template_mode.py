# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-09-10 18:09
from __future__ import unicode_literals

import base.utils
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0070_add_config_id_field_tophase_leaderboard_and_datasetsplit_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500)),
                ('template_file', models.FileField(upload_to=base.utils.RandomFileName('templates'))),
                ('is_active', models.BooleanField(db_index=True, default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to=base.utils.RandomFileName('templates/preview-images/'), verbose_name='Template Preview Image')),
                ('dataset', models.CharField(default='', max_length=200)),
                ('eval_metrics', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), blank=True, default=['Accuracy'], size=None)),
                ('phases', models.IntegerField(blank=True, default=None, null=True)),
                ('splits', models.IntegerField(blank=True, default=None, null=True)),
                ('slug', models.CharField(default='', max_length=500)),
            ],
            options={
                'db_table': 'challenge_templates',
                'ordering': ('-created_at',),
            },
        ),
    ]
