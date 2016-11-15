from recommendation.models import Movie, User, List, Rating, Rate, MovieList
import collections
from recommendation.queries import *
from math import sqrt
import tmdbsimple as tmdb

tmdb.API_KEY = '5880f597a9fab4f284178ffe0e1f0dba'

def get_facebook_friends(user_id):
    pass

def get_similar_profiles(user_id):
    oneGenreSimilarity = User.objects.raw("SELECT user.user_ID FROM user INNER JOIN profile ON profile.user_id = user.user_id INNER JOIN profile_genre ON profile.profile_id = profile_genre.profile_id AND (profile_genre.genre_id = '1' OR profile_genre.genre_id = '5' OR profile_genre.genre_id = '13')")

    usersList = []
    similarUsers = []

    for user in oneGenreSimilarity:
        usersList.append(user.user_id)

    for item, count in collections.Counter(usersList).items():
        if count > 1:
            similarUsers.append(item)
            
    return similarUsers

def pearson_correlation(person1,person2):
    
	# To get both rated items
	both_rated = {}
	for item in get_movie_by_user(person1):
		if item in get_movie_by_user(person2):
			both_rated[item] = 1

	number_of_ratings = len(both_rated)		
	
	# Checking for number of ratings in common
	if number_of_ratings == 0:
		return 0

	# Add up all the preferences of each user
	person1_preferences_sum = sum([get_rate_by_movie(item, person1) for item in both_rated])
	person2_preferences_sum = sum([get_rate_by_movie(item, person2) for item in both_rated])

	# Sum up the squares of preferences of each user
	person1_square_preferences_sum = sum([pow(get_rate_by_movie(item, person1),2) for item in both_rated])
	person2_square_preferences_sum = sum([pow(get_rate_by_movie(item, person2),2) for item in both_rated])

	# Sum up the product value of both preferences for each item
	product_sum_of_both_users = sum([get_rate_by_movie(item, person1) * get_rate_by_movie(item, person2) for item in both_rated])


	# Calculate the pearson score
	numerator_value = product_sum_of_both_users - (person1_preferences_sum*person2_preferences_sum/number_of_ratings)
	denominator_value = sqrt((person1_square_preferences_sum - pow(person1_preferences_sum,2)/number_of_ratings) * (person2_square_preferences_sum -pow(person2_preferences_sum,2)/number_of_ratings))
	if denominator_value == 0:
		return 0
	else:
		r = numerator_value/denominator_value
		return r 

def most_similar_users(person,number_of_users):
	# returns the number_of_users (similar persons) for a given specific person.
	dataset = get_similar_profiles(person)
	scores = [(pearson_correlation(person,other_person),other_person) for other_person in dataset if  other_person != person ]
	
	# Sort the similar persons so that highest scores person will appear at the first
	scores.sort()
	scores.reverse()
	return scores[0:number_of_users]

def user_recommendations(person):
	dataset = get_similar_profiles(person)
	# Gets recommendations for a person by using a weighted average of every other user's rankings
	totals = {}
	simSums = {}
	rankings_list =[]
	for other in dataset:
		# don't compare me to myself
		if other == person:
			continue
		sim = pearson_correlation(person,other)

		# ignore scores of zero or lower
		if sim <=0: 
			continue
		for item in get_movie_by_user(other):

			# only score movies i haven't seen yet
			if item not in get_movie_by_user(person):

			# Similrity * score
				totals.setdefault(item,0)
				totals[item] += get_rate_by_movie(item, other)* sim
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

def add_recommentation_to_database(user):
	recommendation = build_recommendation_dataset(user)
	list_id = get_list_by_user(user, 1)

	movies =[]

	for item in movie_by_user_list(user,'recommendation'):
		movies.append(item.movie_id)
   
	for item in recommendation:
		if item not in movies:
			reco = MovieList(movie_id=item, list_id=list_id)
			reco.save()

def get_similar_movies(tmdb_movie_id):
	similar_movies = []
	movie = tmdb.Movies(tmdb_movie_id)
	response = movie.similar_movies(page=1, append_to_response='top_rated')

	for item in response['results']:
		similar_movies.append(item['id'])

	return similar_movies

def filter_movies(movies, user):
	user_movies = get_tmdb_movies_id_by_user(user)

	for item in movies:
		if item in user_movies:
			movies.remove(item)
	return movies

def add_movie_to_database(movie):
	if movie not in get_tmdb_movies_id():
		movie_db = Movie(tmdb_movie_id=movie)
		movie_db.save()

def get_tmdb_movies(id_movie_list):
	tmdb_movies = []
	for item in id_movie_list:
		tmdb_movies.append(get_tmdb_movie_id_by_movie(item))

	return tmdb_movies

def get_movie_id(tmdb_movie_list):
	id_movie_list = []
	for item in tmdb_movie_list:
		id_movie_list.append(get_movie_id_by_tmdb_id(item))
	
	return id_movie_list

def build_recommendation_dataset(user):
	recommendation = user_recommendations(user)
	reco = get_tmdb_movies(recommendation)
	similar_movies = []

	for movie in reco:
		similar_movies =  similar_movies + get_similar_movies(movie)
	
	full_recommendation = similar_movies + reco
	full_recommendation = filter_movies(full_recommendation, user)
	full_recommendation = list(set(full_recommendation))

	for item in full_recommendation:
		add_movie_to_database(item)

	id_recommendation_list = get_movie_id(full_recommendation)


	return id_recommendation_list
	