# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corpus',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('source', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('time', models.CharField(max_length=15)),
                ('tag', models.CharField(max_length=150)),
                ('orgranization', models.CharField(max_length=150)),
                ('language', models.CharField(max_length=50)),
                ('target', models.TextField()),
            ],
        ),
    ]
