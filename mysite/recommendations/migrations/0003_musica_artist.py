# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0002_album_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='artist',
            field=models.CharField(default='Anitta', max_length=20),
            preserve_default=False,
        ),
    ]
