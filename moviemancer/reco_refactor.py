# -*- coding: utf-8 -*-

from math import sqrt
from moviemancer.models import Movie, Viwer, List, Rating, Rate, MovieList
import collections
from moviemancer.queries import *
from math import sqrt
import tmdbsimple as tmdb

tmdb.API_KEY = '5880f597a9fab4f284178ffe0e1f0dba'

def get_dataset():
    users = Viwer.objects.all()
    dataset = {}

    for user in users:
        movies = get_rated_movies_by_user(user.user_id)
        dataset.update({user.user_id: movies})

    return dataset

def get_higher_rated(user_id):
    higher_rated_list = []
    movies = []
    for item in movie_id_by_user_list(user_id, 3):
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

def convert_tmdb_rating(tmdb_rating):
    return int(round(tmdb_rating/2))

def get_tmdb_similar_movies(tmdb_movie_id):
    similar_movies = []
    movie = tmdb.Movies(tmdb_movie_id)
    response = movie.similar_movies(language = 'pt-BR', page=1)

    for item in response['results']:
        year = item['release_date'].split('-')
        year = year[0]

        poster = 'http://image.tmdb.org/t/p/original' + item['poster_path']

        genres = []
        for g in item['genre_ids']:
            genres.append(str(g))

        genres = ','.join(genres)

        r = item['vote_average']
        r = int(r)

        if r == 1 or r == 2:
            r = 1
        if r == 3 or r == 4:
            r = 2
        if r == 5 or r == 6:
            r = 3
        if r == 7 or r == 8:
            r = 4
        if r == 9 or r == 10:
            r = 5

        similar_movies.append({ "tmdb_movie_id": item['id'], 
                                "language": item['original_language'],
                                "rating": r,
                                "year": year, 
                                "poster": poster, 
                                "title": item['title'],
                                "genres": genres
                                })
	
    return similar_movies

def add_ready_movie_to_database(movie):
    
    tmdb_id = movie['tmdb_movie_id']
    if not Movie.objects.filter(tmdb_movie_id = tmdb_id):
        tmdb_poster = movie['poster']
        tmdb_title = movie['title']
        tmdb_rating = movie['rating']
        tmdb_language = movie['language']
        tmdb_runtime = get_tmdb_movie_runtime(tmdb_id)
        tmdb_genres = movie['genres']
        tmdb_year = movie['year']

        movie_db = Movie(tmdb_movie_id=tmdb_id, tmdb_poster = tmdb_poster, tmdb_title = tmdb_title, tmdb_rating = tmdb_rating, language = tmdb_language, year = tmdb_year, genres = tmdb_genres, runtime = tmdb_runtime)
        
        try:
            movie_db.save()
        except:
            print('Deu ruim at: ', tmdb_id)

def get_similar_movies(movie_id):
    similar_movies = []
    
    tmdb_movie_id = get_tmdb_movie_id_by_movie(movie_id)

    tmdb_similar_movies = get_tmdb_similar_movies(tmdb_movie_id)

    for movie in tmdb_similar_movies:
        if is_movie_on_database(movie['tmdb_movie_id']):
            similar_movies.append(get_movie_id_by_tmdb_id(movie['tmdb_movie_id']))
        else:
            add_ready_movie_to_database(movie)
            similar_movies.append(get_movie_id_by_tmdb_id(movie['tmdb_movie_id']))

    return similar_movies

def is_movie_on_database(tmdb_movie_id):
    movie = Movie.objects.filter(tmdb_movie_id = tmdb_movie_id)

    if not movie:
        return False
    return True

def remove_repeated_recommendations(user_id, reco_list, list_name):
    for item in movie_id_by_user_list(user_id, list_name):
        if item.movie_id in reco_list:
            reco_list.remove(item.movie_id)
    return reco_list

def update_recommendation(user_id):
    #get recommendation by CF
    reco_list = user_recommendations(user_id)
    reco_list = remove_repeated_recommendations(user_id, reco_list, 1)
    reco_list = remove_repeated_recommendations(user_id, reco_list, 2)
    reco_list = remove_repeated_recommendations(user_id, reco_list, 3)

    add_recommendation_to_database(reco_list, user_id)

def generate_recommendation(user_id):
    #get recommendation by CF
    reco_list = user_recommendations(user_id)
    #"compare" with database to see if there are any changes
    reco_list = remove_repeated_recommendations(user_id, reco_list, 1)
    reco_list = remove_repeated_recommendations(user_id, reco_list, 2)
    reco_list = remove_repeated_recommendations(user_id, reco_list, 3)

    reco_list = complete_recommendation(reco_list, user_id)
    add_recommendation_to_database(reco_list, user_id)

def add_recommendation_to_database(reco_list, user_id):
    list_id = get_list_by_user(user_id, 1)
    reco_list = list(set(reco_list))

    for movie_id in reco_list:
        reco = MovieList(movie_id=movie_id, list_id=list_id)

        reco.save()

def complete_recommendation(reco_list, user_id):
    list_id = get_list_by_user(user_id, 1)
    if len(MovieList.objects.filter(list_id = list_id)) < 54:
        higher_rated = get_higher_rated(user_id)

        reco_list = reco_list + get_similar_movies(higher_rated[0])
        time.sleep(1)
        reco_list = reco_list + get_similar_movies(higher_rated[1])
        
        #remove repeated values
        reco_list = list(set(reco_list))
        #remove repeated entries
        reco_list = remove_repeated_recommendations(user_id, reco_list, 1)
        reco_list = remove_repeated_recommendations(user_id, reco_list, 2)
        reco_list = remove_repeated_recommendations(user_id, reco_list, 3)

    return reco_list