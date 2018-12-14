# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_id', models.IntegerField(db_column='user_id')),
                ('movie_id', models.IntegerField(db_column='movie_id')),
                ('comment', models.TextField()),
            ],
            options={
                'db_table': 'comments',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('list_id', models.AutoField(serialize=False, primary_key=True, db_column='list_id')),
                ('user_id', models.IntegerField(db_column='user_id')),
                ('type_id', models.IntegerField(db_column='type_id')),
            ],
            options={
                'db_table': 'list',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.AutoField(serialize=False, primary_key=True, db_column='movie_id')),
                ('tmdb_movie_id', models.BigIntegerField(db_column='tmdb_movie_id')),
                ('tmdb_poster', models.CharField(max_length=255)),
                ('tmdb_title', models.CharField(max_length=255)),
                ('tmdb_rating', models.IntegerField(db_column='tmdb_rating')),
                ('year', models.IntegerField(db_column='year')),
                ('runtime', models.IntegerField(db_column='runtime')),
                ('language', models.CharField(max_length=200)),
                ('genres', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'movie',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('movie_list_id', models.AutoField(serialize=False, primary_key=True, db_column='movie_list_id')),
                ('movie_id', models.IntegerField(db_column='movie_id')),
                ('list_id', models.IntegerField(db_column='list_id')),
            ],
            options={
                'db_table': 'movie_list',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('rate_id', models.AutoField(serialize=False, primary_key=True, db_column='rate_id')),
                ('rate', models.IntegerField()),
            ],
            options={
                'db_table': 'rate',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('rating_id', models.AutoField(serialize=False, primary_key=True, db_column='rating_id')),
                ('user_id', models.IntegerField(db_column='user_id')),
                ('movie_id', models.IntegerField(db_column='movie_id')),
                ('rate_id', models.IntegerField(db_column='rate_id')),
            ],
            options={
                'db_table': 'rating',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('type_id', models.AutoField(serialize=False, primary_key=True, db_column='type_id')),
                ('type_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'type',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Viwer',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True, db_column='user_id')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'viwer',
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
