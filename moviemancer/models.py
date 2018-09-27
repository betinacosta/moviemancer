# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(db_column='user_id')
    movie_id = models.IntegerField(db_column='movie_id')
    comment = models.TextField()

    class Meta:
        managed = True
        db_table = 'comments'

class List(models.Model):
    list_id = models.AutoField(db_column='list_id', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='user_id')  # Field name made lowercase.
    type_id = models.IntegerField(db_column='type_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'list'

class Movie(models.Model):
    movie_id = models.AutoField(db_column='movie_id', primary_key=True)  # Field name made lowercase.
    tmdb_movie_id = models.BigIntegerField(db_column='tmdb_movie_id')  # Field name made lowercase.
    tmdb_poster = models.CharField(max_length=255)
    tmdb_title = models.CharField(max_length=255)
    tmdb_rating = models.IntegerField(db_column='tmdb_rating')
    year = models.IntegerField(db_column='year')
    runtime = models.IntegerField(db_column='runtime')
    language = models.CharField(max_length=200)
    genres = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'movie'

class MovieList(models.Model):
    movie_list_id = models.AutoField(db_column='movie_list_id', primary_key=True)  # Field name made lowercase.
    movie_id = models.IntegerField(db_column='movie_id')  # Field name made lowercase.
    list_id = models.IntegerField(db_column='list_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'movie_list'

class Rate(models.Model):
    rate_id = models.AutoField(db_column='rate_id', primary_key=True)  # Field name made lowercase.
    rate = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'rate'

class Rating(models.Model):
    rating_id = models.AutoField(db_column='rating_id', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='user_id')  # Field name made lowercase.
    movie_id = models.IntegerField(db_column='movie_id') # Field name made lowercase.
    rate_id = models.IntegerField(db_column='rate_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'rating'

class Type(models.Model):
    type_id = models.AutoField(db_column='type_id', primary_key=True)  # Field name made lowercase.
    type_name = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'type'

class Viwer(models.Model):
    user_id = models.AutoField(db_column='user_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=500)

    class Meta:
        managed = True
        db_table = 'viwer'