from __future__ import unicode_literals

from django.db import models


class Cast(models.Model):
    cast_id = models.AutoField(db_column='cast_ID', primary_key=True)  # Field name made lowercase.
    tmdb_cast_id = models.IntegerField(db_column='tmdb_cast_ID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'cast'


class Genre(models.Model):
    genre_id = models.AutoField(db_column='genre_ID', primary_key=True)  # Field name made lowercase.
    tmdb_genre_id = models.IntegerField(db_column='tmdb_genre_ID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'genre'


class List(models.Model):
    list_id = models.AutoField(db_column='list_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user_ID')  # Field name made lowercase.
    type = models.ForeignKey('Type', models.DO_NOTHING, db_column='type_ID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'list'


class Movie(models.Model):
    movie_id = models.AutoField(db_column='movie_ID', primary_key=True)  # Field name made lowercase.
    tmdb_movie_id = models.IntegerField(db_column='tmdb_movie_ID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'movie'


class MovieList(models.Model):
    movie_list_id = models.AutoField(db_column='movie_list_ID', primary_key=True)  # Field name made lowercase.
    movie = models.ForeignKey(Movie, models.DO_NOTHING, db_column='movie_ID')  # Field name made lowercase.
    list = models.ForeignKey(List, models.DO_NOTHING, db_column='list_ID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'movie_list'


class Profile(models.Model):
    profile_id = models.AutoField(db_column='profile_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user_ID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'profile'


class ProfileCast(models.Model):
    profile_cast_id = models.AutoField(db_column='profile_cast_ID', primary_key=True)  # Field name made lowercase.
    profile = models.ForeignKey(Profile, models.DO_NOTHING, db_column='profile_ID')  # Field name made lowercase.
    cast = models.ForeignKey(Cast, models.DO_NOTHING, db_column='cast_ID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'profile_cast'


class ProfileGenre(models.Model):
    profile_genre_id = models.AutoField(db_column='profile_genre_ID', primary_key=True)  # Field name made lowercase.
    profile = models.ForeignKey(Profile, models.DO_NOTHING, db_column='profile_ID')  # Field name made lowercase.
    genre = models.ForeignKey(Genre, models.DO_NOTHING, db_column='genre_ID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'profile_genre'


class Rate(models.Model):
    rate_id = models.AutoField(db_column='rate_ID', primary_key=True)  # Field name made lowercase.
    rate = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'rate'


class Rating(models.Model):
    rating_id = models.AutoField(db_column='rating_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user_ID')  # Field name made lowercase.
    movie = models.ForeignKey(Movie, models.DO_NOTHING, db_column='movie_ID')  # Field name made lowercase.
    rate = models.ForeignKey(Rate, models.DO_NOTHING, db_column='rate_ID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'rating'


class Type(models.Model):
    type_id = models.AutoField(db_column='type_ID', primary_key=True)  # Field name made lowercase.
    type_name = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'type'


class User(models.Model):
    user_id = models.AutoField(db_column='user_ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'user'