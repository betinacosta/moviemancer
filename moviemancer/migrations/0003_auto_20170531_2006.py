# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviemancer', '0002_auto_20160919_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('cast_id', models.AutoField(serialize=False, primary_key=True, db_column='cast_ID')),
                ('tmdb_cast_id', models.IntegerField(db_column='tmdb_cast_ID')),
            ],
            options={
                'db_table': 'cast',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.AutoField(serialize=False, primary_key=True)),
                ('comment', models.TextField()),
            ],
            options={
                'db_table': 'comments',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.AutoField(serialize=False, primary_key=True, db_column='genre_ID')),
                ('tmdb_genre_id', models.IntegerField(db_column='tmdb_genre_ID')),
            ],
            options={
                'db_table': 'genre',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('list_id', models.AutoField(serialize=False, primary_key=True, db_column='list_ID')),
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
                ('movie_id', models.AutoField(serialize=False, primary_key=True, db_column='movie_ID')),
                ('tmdb_movie_id', models.IntegerField(db_column='tmdb_movie_ID')),
                ('tmdb_poster', models.CharField(max_length=255)),
                ('tmdb_title', models.CharField(max_length=255)),
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
                ('movie_list_id', models.AutoField(serialize=False, primary_key=True, db_column='movie_list_ID')),
                ('list', models.ForeignKey(to='recommendation.List', db_column='list_ID', to_field=django.db.models.deletion.DO_NOTHING)),
                ('movie', models.ForeignKey(to='recommendation.Movie', db_column='movie_ID', to_field=django.db.models.deletion.DO_NOTHING)),
            ],
            options={
                'db_table': 'movie_list',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_id', models.AutoField(serialize=False, primary_key=True, db_column='profile_ID')),
            ],
            options={
                'db_table': 'profile',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfileCast',
            fields=[
                ('profile_cast_id', models.AutoField(serialize=False, primary_key=True, db_column='profile_cast_ID')),
                ('cast', models.ForeignKey(to='recommendation.Cast', db_column='cast_ID', to_field=django.db.models.deletion.DO_NOTHING)),
                ('profile', models.ForeignKey(to='recommendation.Profile', db_column='profile_ID', to_field=django.db.models.deletion.DO_NOTHING)),
            ],
            options={
                'db_table': 'profile_cast',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfileGenre',
            fields=[
                ('profile_genre_id', models.AutoField(serialize=False, primary_key=True, db_column='profile_genre_ID')),
                ('genre', models.ForeignKey(to='recommendation.Genre', db_column='genre_ID', to_field=django.db.models.deletion.DO_NOTHING)),
                ('profile', models.ForeignKey(to='recommendation.Profile', db_column='profile_ID', to_field=django.db.models.deletion.DO_NOTHING)),
            ],
            options={
                'db_table': 'profile_genre',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('rate_id', models.AutoField(serialize=False, primary_key=True, db_column='rate_ID')),
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
                ('rating_id', models.AutoField(serialize=False, primary_key=True, db_column='rating_ID')),
                ('movie', models.ForeignKey(to='recommendation.Movie', db_column='movie_ID', to_field=django.db.models.deletion.DO_NOTHING)),
                ('rate', models.ForeignKey(to='recommendation.Rate', db_column='rate_ID', to_field=django.db.models.deletion.DO_NOTHING)),
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
            name='User',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True, db_column='user_ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(to='recommendation.User', db_column='user_ID', to_field=django.db.models.deletion.DO_NOTHING),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(to='recommendation.User', db_column='user_ID', to_field=django.db.models.deletion.DO_NOTHING),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='list',
            name='type',
            field=models.ForeignKey(to='recommendation.Type', db_column='type_ID', to_field=django.db.models.deletion.DO_NOTHING),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='list',
            name='user',
            field=models.ForeignKey(to='recommendation.User', db_column='user_ID', to_field=django.db.models.deletion.DO_NOTHING),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='movie',
            field=models.ForeignKey(to='recommendation.Movie', to_field=django.db.models.deletion.DO_NOTHING),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(to='recommendation.User', to_field=django.db.models.deletion.DO_NOTHING),
            preserve_default=True,
        ),
    ]
