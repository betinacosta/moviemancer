from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from django.contrib import admin
admin.autodiscover()

import moviemancer.views

urlpatterns = [
    url(r'^$', moviemancer.views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^movies/$', moviemancer.views.MovieView.as_view(), name='movies'),
    url(r'^moviemancer/$', moviemancer.views.moviemancer, name='moviemancer'),
    url(r'^recommendation/$', moviemancer.views.recommendation, name='recommendation'),
    url(r'^ratemovie/$', moviemancer.views.ratemovie, name='ratemovie'),
    url(r'^moviedetails/$', moviemancer.views.moviedetails, name='moviedetails'),
    url(r'^addwatchlist/$', moviemancer.views.add_watchlist, name='addwatchlist'),
    url(r'^addwatchlistexternal/$', moviemancer.views.add_watchlist_external, name='addwatchlistexternal'),
    url(r'^rateexternalmovie/$', moviemancer.views.rate_external, name='rateexternalmovie'),
    url(r'^watchedlist/$', moviemancer.views.show_watched_list, name='watchedlist'),
    url(r'^getwatchedlist/$', moviemancer.views.get_watched_list, name='getwatchedlist'),
    url(r'^removefromwatchedlist/$', moviemancer.views.remove_from_watched_list, name='removefromwatchedlist'),
    url(r'^removefromwatchlist/$', moviemancer.views.remove_from_watchlist, name='removefromwatchlist'),
    url(r'^watchlist/$', moviemancer.views.show_watchlist, name='watchlist'),
    url(r'^getwatchlist/$', moviemancer.views.get_watch_list, name='getwatchlist'),
    url(r'^filters/$', moviemancer.views.show_filters, name='filters'),
    url(r'^login/$', moviemancer.views.show_login, name='login'),
    url(r'^singup/$', moviemancer.views.show_singup, name='singup'),
    url(r'^authentication/$', moviemancer.views.get_auth, name='authentication'),
    url(r'^registration/$', moviemancer.views.registration, name='registration'),
    url(r'^getrecommendation/$', moviemancer.views.get_recommendation, name='getrecommendation'),
    url(r'^registergenres/$', moviemancer.views.register_genres, name='registergenres'),
    url(r'^validateuser/$', moviemancer.views.validate_user, name='validateuser'),
    url(r'^profile/$', moviemancer.views.profile, name='profile'),
    url(r'^getprofile/$', moviemancer.views.get_profile, name='getprofile'),
    url(r'^updateuser/$', moviemancer.views.update_user, name='updateuser'),
    url(r'^updategenres/$', moviemancer.views.update_genres, name='updategenres'),
    url(r'^getcomments/$', moviemancer.views.get_all_comments, name='getcomments'),
    url(r'^addcomment/$', moviemancer.views.add_new_comment, name='addcomment'),
    url(r'^deletecomment/$', moviemancer.views.delete_user_comment, name='deletecomment'),
    url(r'^search/$', moviemancer.views.search, name='search'),
    url(r'^getratedmovies/$', moviemancer.views.get_rated, name='getratedmovies'),
    url(r'^notfound/$', moviemancer.views.notfound, name='notfound'),
    url(r'^filterreco/$', moviemancer.views.filter_reco, name='filterreco'),
    url(r'^ratefirstmovies/$', moviemancer.views.rate_first_movies_request, name='ratefirstmovies'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
