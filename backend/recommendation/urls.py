from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movies/$', views.MovieView.as_view(), name='movies'),
    url(r'^reco/$', views.RecoView.as_view(), name='recommendation'),
    url(r'^main/$', views.main, name='main'),
    url(r'^full-recommendation/$', views.fullreco, name='fullreco'),
    url(r'^ratemovie/$', views.ratemovie, name='ratemovie'),
    url(r'^moviedetails/$', views.moviedetails, name='moviedetails'),
    url(r'^addwatchlist/$', views.add_watchlist, name='addwatchlist'),
    url(r'^addwatchlistexternal/$', views.add_watchlist_external, name='addwatchlistexternal'),
    url(r'^rateexternalmovie/$', views.rate_external, name='rateexternalmovie'),

]

urlpatterns = format_suffix_patterns(urlpatterns)