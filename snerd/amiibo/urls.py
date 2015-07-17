from django.conf.urls import url

from . import views

#you have to add the views created bellow
urlpatterns = [
    # /amiibo/
    url(r'^$', views.IndexView.as_view(), name='index'),    #views.IndexView is the "class-based view" from the views.py file of this app "amiibo"
    # /amiibo/10/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),#or pk instead of amiibo_id??
    #  url(r'^series/(?P<pk>[0-9]+)/$', views.SeriesDetailView.as_view(), name='series_detail'),
    #  url(r'^universe/(?P<pk>[0-9]+)/$', views.UniverseDetailView.as_view(), name='universe_detail'),
]