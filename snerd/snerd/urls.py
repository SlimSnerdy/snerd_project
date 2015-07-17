from django.conf.urls import include, url
from django.contrib import admin

#for development static files
from django.conf import settings
from django.contrib.staticfiles import views
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'snerd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^$', include('amiibo.urls', namespace="amiibo")),                                 #use r'^$' for the domain home
    url(r'^games/',include('games.urls', namespace="games")),                       #games.urls is the urls.py file INSIDE the games APP
    url(r'^ice_cream/', include('ice_cream.urls', namespace="ice_cream")),     #ice_cream.urls is the urls.py file INSIDE the ice_cream APP       
    url(r'^amiibo/', include('amiibo.urls', namespace="amiibo")),                        #amiibo.urls is the urls.py file INSIDE the amiibo APP
    url(r'^admin/', include(admin.site.urls)),              
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#BELOW IS DEVELOPMENT CODE FOR SERVING STATIC FILES; DONT USE IN PRODUCTION!
if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.serve),
    ]     