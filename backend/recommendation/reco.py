from recommendation.models import Movie, User, List, Rating
import collections


def teste():
    query = Movie.objects.all()
    return query

def getFacebookFriends(user_id):
    pass

def getSimilarProfiles(user_id):
    oneGenreSimilarity = User.objects.raw("SELECT user.user_ID FROM user INNER JOIN profile ON profile.user_id = user.user_id INNER JOIN profile_genre ON profile.profile_id = profile_genre.profile_id AND (profile_genre.genre_id = '1' OR profile_genre.genre_id = '5' OR profile_genre.genre_id = '13')")

    usersList = []
    similarUsers = []

    for user in oneGenreSimilarity:
        usersList.append(user.user_id)

    for item, count in collections.Counter(usersList).items():
        if count > 1:
            similarUsers.append(item)
            
    return similarUsers

def getMovieByUser(user_id):
    movies =[]
    for item in List.objects.raw("SELECT list_ID FROM list WHERE user_id = %s AND type_id = 3", [user_id]):
        list_id = item.list_id

    for item in Movie.objects.raw("SELECT * from movie INNER JOIN movie_list ON list_id = %s AND movie_list.movie_id = movie.movie_id", [list_id]):
        movies.append(item.movie_id)

    return movies

def getRatesByMovie(movie_id, user_id):
    for item in Rating.objects.raw("SELECT * FROM rating WHERE rating.user_id = %s AND movie_id = %s", [user_id, movie_id]):
        rate_id = item.rate_id

    for item in Rate.objects.raw("SELECT * FROM rate WHERE rate_id = %s", [rate_id])
        movieRate = item.rate

    return movieRate
    

def generateDataset(user_id):
    dataset = {}
    movies = {}
    similarUsers = getSimilarProfiles(user_id)
    

    for user in similarUsers:
        movieByUser = getMovieByUser(user)
        for movie in movieByUser:
            movieRate = getRatesByMovie(user, movie)
            movies[movie] = movieRate
        dataset[user] = movies

    return dataset



