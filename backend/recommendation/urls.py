from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movies/$', views.MovieView.as_view(), name='movies'),
    url(r'^reco/$', views.RecoView.as_view(), name='recommendation'),
    url(r'^main/$', views.main, name='main'),
]

urlpatterns = format_suffix_patterns(urlpatterns)