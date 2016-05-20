# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-20 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(blank=True, max_length=255, null=True)),
                ('scientific_name', models.CharField(max_length=255)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('accepted', models.BooleanField(default=False)),
                ('unaccepted_reason', models.TextField(blank=True, null=True)),
                ('public', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='plants.Plant')),
            ],
        ),
        migrations.CreateModel(
            name='Taxonomy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('level', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='plant',
            name='taxonomy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plants.Taxonomy'),
        ),
    ]
