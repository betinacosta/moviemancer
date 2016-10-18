from django.shortcuts import render

from recommendation.models import Movie, User
from recommendation.serializers import MovieSerializer, UserSerializer
from rest_framework import generics
from recommendation.reco import teste, getSimilarProfiles
 

def index(request):
    return render(request,'recommendation/home.html')

class MovieView(generics.ListAPIView):
    model = Movie
    #queryset = Movie.objects.all()
    queryset = teste()
    serializer_class = MovieSerializer

class RecoView (generics.ListAPIView):
    model = Movie
    queryset = Movie.objects.raw("SELECT * FROM movie INNER JOIN movie_list ON movie.movie_id = movie_list.movie_id INNER JOIN list ON user_id = '1' AND type_id = '1'")
    serializer_class = MovieSerializer

class SimilarityView (generics.ListAPIView):
    model = User
    queryset = getSimilarProfiles('1')
    serializer_class = UserSerializer
    

def main(request):
    return render(request,'recommendation/partials/main.html')

 

'''def index(request):
    movie_list = Movie.objects.all()
    template = loader.get_template('recommendation/index.html')
    context = {
        'movie_list': movie_list,
    }
    return HttpResponse(template.render(context, request))'''