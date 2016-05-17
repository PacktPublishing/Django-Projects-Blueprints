"""discuss URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.views.generic import TemplateView

from accounts.views import UserRegistrationView
from links.views import HomeView
from links.views import NewSubmissionView
from links.views import SubmissionDetailView
from links.views import NewCommentView
from links.views import NewCommentReplyView
from links.views import UpvoteSubmissionView
from links.views import RemoveUpvoteFromSubmissionView


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^login/$', login, kwargs={'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, kwargs={'next_page': '/login/'}, name='logout'),
    url(r'^register/$', UserRegistrationView.as_view(), name='user-registration'),

    url(r'^new-submission/$', NewSubmissionView.as_view(), name='new-submission'),
    url(r'^submission/(?P<pk>\d+)/$', SubmissionDetailView.as_view(), name='submission-detail'),
    url(r'new-comment/$', NewCommentView.as_view(), name='new-comment'),
    url(r'new-comment-reply/$', NewCommentReplyView.as_view(), name='new-comment-reply'),

    url(r'^upvote/(?P<link_pk>\d+)/$', UpvoteSubmissionView.as_view(), name='upvote-submission'),
    url(r'^upvote/(?P<link_pk>\d+)/remove/$', RemoveUpvoteFromSubmissionView.as_view(), name='remove-upvote'),
]