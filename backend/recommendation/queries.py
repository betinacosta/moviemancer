from recommendation.models import Movie, User, List, Rating, Rate, MovieList, Type

def get_list_id_by_user(user_id):
    lists = []
    for item in List.objects.raw("SELECT list_ID FROM list WHERE user_id = %s", [user_id]):
        lists.append(item.list_id)
    return lists

def movie_by_user_list(user_id, list_name):
    for item in Type.objects.raw("SELECT * FROM type WHERE type_name = %s", [list_name]):
        type_id = item.type_id;

    for item in List.objects.raw("SELECT list_ID FROM list WHERE user_id = %s AND type_id = %s", [user_id, type_id]):
        list_id = item.list_id

    return Movie.objects.raw("SELECT * from movie INNER JOIN movie_list ON list_id = %s AND movie_list.movie_id = movie.movie_id", [list_id])

def get_rate_by_movie(movie_id, user_id):
    for item in Rating.objects.raw("SELECT * FROM rating WHERE rating.user_id = %s AND movie_id = %s", [user_id, movie_id]):
        rate_id = item.rate_id

    for item in Rate.objects.raw("SELECT * FROM rate WHERE rate_id = %s", [rate_id]):
        movieRate = item.rate

    return movieRate

def get_list_by_user(user, list_type):
    for item in List.objects.raw("SELECT list_ID FROM list WHERE user_id = %s AND type_id = %s", [user, list_type]):
        list_id = item.list_id
    return list_id
    
def get_movie_by_user(user_id):
    movies =[]
   
    for item in movie_by_user_list(user_id, 'watchedlist'):
        movies.append(item.movie_id)
    return movies

def get_tmdb_movies_id():
    movies = []

    for item in Movie.objects.all():
        movies.append(item.tmdb_movie_id)

    return movies

def get_tmdb_movie_id_by_movie(movie_id):
    for item in Movie.objects.raw("SELECT * FROM movie WHERE movie_id = %s", [movie_id]):
        return item.tmdb_movie_id

def get_movie_id_by_tmdb_id(tmdb_movie_id):
    for item in Movie.objects.raw("SELECT * FROM movie WHERE tmdb_movie_id = %s", [tmdb_movie_id]):
        return item.movie_id

def get_tmdb_movies_id_by_user(user):
    lists_id = get_list_id_by_user(user)
    movies = []

    for item in lists_id:
        for movie in Movie.objects.raw("SELECT * from movie INNER JOIN movie_list ON list_id = %s AND movie_list.movie_id = movie.movie_id", [item]):
            movies.append(movie.tmdb_movie_id)
    
    return movies
