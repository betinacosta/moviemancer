from django.shortcuts import render

from recommendation.models import Movie
from recommendation.serializers import MovieSerializer
from rest_framework import generics
 

def index(request):
    return render(request,'recommendation/home.html')

class MovieView(generics.ListAPIView):
    model = Movie
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

def main(request):
    return render(request,'recommendation/partials/main.html')
 

'''def index(request):
    movie_list = Movie.objects.all()
    template = loader.get_template('recommendation/index.html')
    context = {
        'movie_list': movie_list,
    }
    return HttpResponse(template.render(context, request))'''