from recommendation.models import Movie, User, List, Rating, Rate, MovieList, Type

def movie_by_user_list(user_id, list_name):
    for item in Type.objects.raw("SELECT * FROM type WHERE type_name = %s", [list_name]):
        type_id = item.type_id;

    for item in List.objects.raw("SELECT list_ID FROM list WHERE user_id = %s AND type_id = %s", [user_id, type_id]):
        list_id = item.list_id

    return Movie.objects.raw("SELECT * from movie INNER JOIN movie_list ON list_id = %s AND movie_list.movie_id = movie.movie_id", [list_id])

def getRatesByMovie(movie_id, user_id):
    for item in Rating.objects.raw("SELECT * FROM rating WHERE rating.user_id = %s AND movie_id = %s", [user_id, movie_id]):
        rate_id = item.rate_id

    for item in Rate.objects.raw("SELECT * FROM rate WHERE rate_id = %s", [rate_id]):
        movieRate = item.rate

    return movieRate

def get_list_by_user(user, list_type):
    for item in List.objects.raw("SELECT list_ID FROM list WHERE user_id = %s AND type_id = %s", [user, list_type]):
		list_id = item.list_id
	return list_id