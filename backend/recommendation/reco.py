from recommendation.models import Movie, User, List
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
    list_id = List.objects.raw("SELECT list_ID FROM list WHERE user_id = 7 AND type_id = 3")
    movies_ids = Movie.objects.raw("SELECT movie_ID from movie_list where list_id = 20")
    

def generateDataset(user_id):
    similarUsers = getSimilarProfiles(user_id)



