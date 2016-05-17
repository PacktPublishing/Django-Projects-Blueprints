"""mmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns 

from main.views import MovieDetailsView
from main.views import MoviesListView
from main.views import NewReviewView

urlpatterns = i18n_patterns(
    url(r'^$', MoviesListView.as_view(), name='movies-list'),
    url(r'^movie/(?P<pk>\d+)/$', MovieDetailsView.as_view(), name='movie-details'),
    url(r'^movie/(?P<movie_pk>\d+)/review/$', NewReviewView.as_view(), name='new-review'),

    url(r'^admin/', admin.site.urls),
)