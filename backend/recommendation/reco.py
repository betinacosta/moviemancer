from recommendation.models import Movie, User

def teste():
    query = Movie.objects.all()
    return query

def getFacebookFriends(user_id):
    pass

def getSimilarProfiles(user_id):
    oneGenreSimilarity = User.objects.raw("SELECT distinct user.user_ID FROM user INNER JOIN profile ON profile.user_id = user.user_id INNER JOIN profile_genre ON profile.profile_id = profile_genre.profile_id AND (profile_genre.genre_id = '1' OR profile_genre.genre_id = '5' OR profile_genre.genre_id = '13')")

    return oneGenreSimilarity