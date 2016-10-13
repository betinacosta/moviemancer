from recommendation.models import Movie

def teste():
    query = Movie.objects.all()
    return query