from recommendation.models import Movie, User, List, Rating, Rate, MovieList, Type

def get_list_id_by_user(user_id):
    lists = []
    for item in List.objects.raw("SELECT list_ID FROM list WHERE user_id = %s", [user_id]):
        lists.append(item.list_id)
    return lists

def movie_by_user_list(user_id, list_name):
    list_id = 0
    for item in Type.objects.raw("SELECT * FROM type WHERE type_name = %s", [list_name]):
        type_id = item.type_id

    for item in List.objects.filter(user_id = user_id, type_id = type_id):
        list_id = item.list_id

    movie_list = Movie.objects.raw("SELECT * from movie INNER JOIN movie_list ON list_id = %s AND movie_list.movie_id = movie.movie_id", [list_id])
    return movie_list

def get_rate_by_movie(movie_id, user_id):
    rate_id = 0
    movie_rate = 0
    for item in Rating.objects.raw("SELECT * FROM rating WHERE rating.user_id = %s AND movie_id = %s", [user_id, movie_id]):
        rate_id = item.rate_id

    for item in Rate.objects.raw("SELECT * FROM rate WHERE rate_id = %s", [rate_id]):
        movie_rate = item.rate

    return movie_rate

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

def is_movie_on_list (user_id, movie_id, list_type):
    list_id = get_list_by_user(user_id, list_type)

    movie_list = MovieList.objects.filter(movie_id = movie_id, list_id = list_id)

    if not movie_list:
        return False
    else:
        return True

#UPDATE, DELETE, INSERT

def add_rating_to_movie(user_id, movie_id, local_rate_id):
    rating_query = Rating.objects.filter(movie_id = movie_id, user_id= user_id)

    if not rating_query:
        user_rating = Rating(user_id = user_id, movie_id = movie_id, rate_id = local_rate_id)
        print (user_rating)
        user_rating.save()
    else:
        for item in rating_query:
            user_rating = Rating(rating_id = item.rating_id, user_id = user_id, movie_id = movie_id, rate_id = local_rate_id)
            user_rating.save()

def remove_movie_from_list(user_id, movie_id, list_type):
    list_id = get_list_by_user(user_id, list_type)

    MovieList.objects.filter(movie_id = movie_id, list_id = list_id).delete()

def add_to_watched_list (user_id, movie_id):
    list_id = get_list_by_user(user_id, 3)

    movie_list_entry = MovieList(movie_id = movie_id, list_id = list_id)
    movie_list_entry.save()

def rate_movie (user_id, movie_id, local_rate_id):
    #add rating
    add_rating_to_movie(user_id, movie_id, local_rate_id)

    #check if it is on recommended list and remove it
    if is_movie_on_list (user_id, movie_id, 1):
        remove_movie_from_list(user_id, movie_id, 1)
    #check if it is on watchlist and remove it
    elif is_movie_on_list(user_id, movie_id, 2):
        remove_movie_from_list(user_id, movie_id, 2)

    #add to watched list
    add_to_watched_list (user_id, movie_id)
