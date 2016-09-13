# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='corpus',
            old_name='orgranization',
            new_name='organization',
        ),
    ]
