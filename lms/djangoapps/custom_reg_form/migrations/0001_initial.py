# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-08 23:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=100, verbose_name=b'Branch', error_messages={b'required': 'Please tell us your branch.', b'invalid': "This branch seems to be not available."})),
                ('enrollment_year', models.CharField(choices=[(b'1', b'1st'), (b'2', b'2nd'), (b'3', b'3rd'), (b'4', b'4th')], max_length=5, verbose_name=b'Enrollment Year', error_messages={b'required': 'Enter your enrollment year.', b'invalid': "Not a valid year."})),
                ('preferred_language', models.CharField(max_length=100, verbose_name=b'Preferred Language', error_messages={b'required': 'Enter your preferred language.', b'invalid': "You may have entered a non-existent language."})),
                ('preferred_multimedia', models.CharField(max_length=100, verbose_name=b'Preferred Multimedia', error_messages={b'required': 'Your preferred medium.', b'invalid': "You have entered a non-existent multimedia."})),
                ('interests', models.CharField(choices=[(b'coding', b'Coding'), (b'reading', b'Reading'), (b'sports', b'Sports'), (b'music', b'Music'), (b'dance', b'Dance'), (b'data science', b'Data Science'), (b'ai/ml', b'AI/ML'), (b'iot', b'IoT'), (b'cyber security', b'Cyber Security'), (b'video development', b'Video Development'), (b'databases', b'Databases'), (b'python', b'Python'), (b'java', b'Java'), (b'open source', b'Open Source'), (b'others', b'Others')], max_length=100, verbose_name=b'Your Interests', error_messages={b'required': 'Your interests.', b'invalid': "You have entered some invalid interests."})),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

