# -*- coding: utf-8 -*-
from moviemancer.models import *
from moviemancer.helpers import Helpers
from moviemancer.recommendation import Recommendation
from math import sqrt

def get_dataset():
    users = Viwer.objects.all()
    dataset = {}

    for user in users:
        movies = Helpers.get_rated_movies_by_user(user.user_id)
        dataset.update({user.user_id: movies})

    return dataset

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
    recommendation = [recommend_item for score,recommend_item in rankings]
    return recommendation

def remove_repeated_recommendations(user_id, reco_list, list_name):
    for item in Helpers.movie_id_by_user_list(user_id, list_name):
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
    list_id = Helpers.get_user_list_id_by_type_id(user_id, 1)
    reco_list = list(set(reco_list))

    for movie_id in reco_list:
        reco = MovieList(movie_id=movie_id, list_id=list_id)

        reco.save()

def complete_recommendation(reco_list, user_id):
    list_id = Helpers.get_user_list_id_by_type_id(user_id, 1)
    if len(MovieList.objects.filter(list_id = list_id)) < 54:
        higher_rated = Helpers.get_best_ratted_movies_by_user(user_id=user_id, trashold=3)

        reco_list = reco_list + Recommendation.get_similar_movies(higher_rated[0])
        reco_list = reco_list + Recommendation.get_similar_movies(higher_rated[1])

        #remove repeated values
        reco_list = list(set(reco_list))
        #remove repeated entries
        reco_list = remove_repeated_recommendations(user_id, reco_list, 1)
        reco_list = remove_repeated_recommendations(user_id, reco_list, 2)
        reco_list = remove_repeated_recommendations(user_id, reco_list, 3)

    return reco_list