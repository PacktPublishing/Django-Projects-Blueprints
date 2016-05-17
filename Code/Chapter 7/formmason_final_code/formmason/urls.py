from django.conf.urls import url

from main.views import CreateEditFormView
from main.views import CustomFormView
from main.views import FormResponsesListView
from main.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^form/(?P<form_pk>\d+)/$', CustomFormView.as_view(), name='custom-form'),
    url(r'^form/(?P<form_pk>\d+)/responses/$', FormResponsesListView.as_view(), name='form-responses'),

    url(r'form/new/$', CreateEditFormView.as_view(), name='create-form'),
    url(r'form/(?P<form_pk>\d+)/edit/$', CreateEditFormView.as_view(), name='edit-form'),
]