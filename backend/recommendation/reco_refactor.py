from math import sqrt
from recommendation.models import Movie, User, List, Rating, Rate, MovieList
import collections
from recommendation.queries import *
from math import sqrt
import tmdbsimple as tmdb

tmdb.API_KEY = '5880f597a9fab4f284178ffe0e1f0dba'

def get_dataset():
    users = User.objects.all()
    dataset = {}

    for user in users:
        movies = get_rated_movies_by_user(user.user_id)
        dataset.update({user.user_id: movies})

    return dataset

def get_higher_rated(user_id):
    higher_rated_list = []
    movies = []
    for item in movie_by_user_list(user_id, 'watchedlist'):
        movies.append(item.movie_id)

    for movie in movies:
        rate = get_rate_by_movie(movie, user_id)
        if rate > 2:
            higher_rated_list.append(movie)

    return higher_rated_list

def person_correlation(person1, person2, dataset):

   # To get both rated items
    both_rated = {}
    for item in dataset[person1]:
        if item in dataset[person2]:
            both_rated[item] = 1

    number_of_ratings = len(both_rated)

    # Checking for ratings in common
    if number_of_ratings == 0:
        return 0

    # Add up all the preferences of each user
    person1_preferences_sum = sum([dataset[person1][item] for item in both_rated])
    person2_preferences_sum = sum([dataset[person2][item] for item in both_rated])

    # Sum up the squares of preferences of each user
    person1_square_preferences_sum = sum([pow(dataset[person1][item],2) for item in both_rated])
    person2_square_preferences_sum = sum([pow(dataset[person2][item],2) for item in both_rated])

    # Sum up the product value of both preferences for each item
    product_sum_of_both_users = sum([dataset[person1][item] * dataset[person2][item] for item in both_rated])

    # Calculate the pearson score
    numerator_value = product_sum_of_both_users - (person1_preferences_sum*person2_preferences_sum/number_of_ratings)
    denominator_value = sqrt((person1_square_preferences_sum - pow(person1_preferences_sum,2)/number_of_ratings) * (person2_square_preferences_sum -pow(person2_preferences_sum,2)/number_of_ratings))

    if denominator_value == 0:
        return 0
    else:
        r = numerator_value / denominator_value
        return r

def user_recommendations(person):

    # Gets recommendations for a person by using a weighted average of every other user's rankings
    totals = {}
    simSums = {}
    rankings_list =[]
    dataset = get_dataset()

    for other in dataset:
        # don't compare me to myself
        if other == person:
            continue
        sim = person_correlation(person,other,dataset)
        #print ">>>>>>>",sim

        # ignore scores of zero or lower
        if sim <=0: 
            continue
        for item in dataset[other]:

            # only score movies i haven't seen yet
            if item not in dataset[person] or dataset[person][item] == 0:

            # Similrity * score
                totals.setdefault(item,0)
                totals[item] += dataset[other][item]* sim
                # sum of similarities
                simSums.setdefault(item,0)
                simSums[item]+= sim

        # Create the normalized list

    rankings = [(total/simSums[item],item) for item,total in totals.items()]
    rankings.sort()
    rankings.reverse()
    # returns the recommended items
    recommendataions_list = [recommend_item for score,recommend_item in rankings]
    return recommendataions_list

def get_tmdb_similar_movies(tmdb_movie_id):
    similar_movies = []
    movie = tmdb.Movies(tmdb_movie_id)
    response = movie.similar_movies(page=1)

    for item in response['results']:
        similar_movies.append(item['id'])
	
    return similar_movies

def get_tmdb_poster(tmdb_movie_id):
    movie = tmdb.Movies(tmdb_movie_id)
    response = movie.info(language='pt-BR')
    path = 'http://image.tmdb.org/t/p/original' + response["poster_path"]

    return path

def get_tmdb_title(tmdb_movie_id):
	movie = tmdb.Movies(tmdb_movie_id)
	response = movie.info(language='pt-BR')
	title = response["title"]

	return title

def add_movie_to_database(movie):
    title = get_tmdb_title(movie)
    poster = get_tmdb_poster(movie)
    
    movie_db = Movie(tmdb_movie_id=movie, tmdb_poster=poster, tmdb_title=title)
    movie_db.save()

def get_similar_movies(movie_id):
    similar_movies = []
    
    tmdb_movie_id = get_tmdb_movie_id_by_movie(movie_id)

    tmdb_similar_movies = get_tmdb_similar_movies(tmdb_movie_id)

    for tmdb_id in tmdb_similar_movies:
        if is_movie_on_database(tmdb_id):
            similar_movies.append(get_movie_id_by_tmdb_id(tmdb_id))
        else:
            add_movie_to_database(tmdb_id)
            similar_movies.append(get_movie_id_by_tmdb_id(tmdb_id))

    return similar_movies

def is_movie_on_database(tmdb_movie_id):
    movie = Movie.objects.filter(tmdb_movie_id = tmdb_movie_id)

    if not movie:
        return False
    else:
        return True

def remove_repeated_recommendations(user_id, reco_list, list_name):
    for item in movie_by_user_list(user_id, 'recommendation'):
        if item.movie_id in reco_list:
            reco_list.remove(item.movie_id)
    return reco_list

def update_recommendation(user_id):
    #get recommendation by CF
    reco_list = user_recommendations(user_id)
    reco_list = remove_repeated_recommendations(user_id, reco_list, 'recommendation')
    reco_list = remove_repeated_recommendations(user_id, reco_list, 'watchlist')
    reco_list = remove_repeated_recommendations(user_id, reco_list, 'watchedlist')

    add_recommendation_to_database(reco_list, user_id)

def generate_recommendation(user_id):
    #get recommendation by CF
    reco_list = user_recommendations(user_id)
    print '1. reco_list: ', reco_list

    #check if there are item that are already in the user recommendation or watchlist and remove it
    reco_list = remove_repeated_recommendations(user_id, reco_list, 'recommendation')
    reco_list = remove_repeated_recommendations(user_id, reco_list, 'watchlist')
    reco_list = remove_repeated_recommendations(user_id, reco_list, 'watchedlist')
    
    #check if there are enough recommendations
    if len(reco_list) < 100:
        higher_rated = get_higher_rated(user_id)
        print '1. higher_rated: ', higher_rated

        if len(higher_rated) > 2:
            for i in range(0,2):
                reco_list = reco_list + get_similar_movies(higher_rated[i])
        else:
            for movie_id in higher_rated:
                reco_list = reco_list + get_similar_movies(movie_id)
        #remove repeated values
        reco_list = list(set(reco_list))
        #remove repeated entries
        reco_list = remove_repeated_recommendations(user_id, reco_list, 'recommendation')
        reco_list = remove_repeated_recommendations(user_id, reco_list, 'watchlist')
        reco_list = remove_repeated_recommendations(user_id, reco_list, 'watchedlist')

    add_recommendation_to_database(reco_list, user_id)

def add_recommendation_to_database(reco_list, user_id):
    list_id = get_list_by_user(user_id, 1)

    for movie_id in reco_list:
        reco = MovieList(movie_id=movie_id, list_id=list_id)
        reco.save()
            

    
    

    


        
        


