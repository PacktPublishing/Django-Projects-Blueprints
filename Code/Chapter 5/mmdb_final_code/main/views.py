from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.utils.translation import get_language

from main.models import MovieDetails
from main.models import MovieReview


class MoviesListView(ListView):
    model = MovieDetails
    template_name = 'movies_list.html'

    def get(self, request, *args, **kwargs):
        current_language = get_language()
        request.session[LANGUAGE_SESSION_KEY] = current_language

        return super(MoviesListView, self).get(request, *args, **kwargs)


class MovieDetailsView(DetailView):
    model = MovieDetails
    template_name = 'movie_details.html'


class NewReviewView(CreateView):
    model = MovieReview
    fields = ['user_name', 'review']

    template_name = 'new_movie_review.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewReviewView, self).get_context_data(**kwargs)

        movie_pk = self.kwargs['movie_pk']
        movie = MovieDetails.objects.get(pk=movie_pk)
        ctx['movie'] = movie

        return ctx

    def form_valid(self, form):
        movie_pk = self.kwargs['movie_pk']
        movie = MovieDetails.objects.get(pk=movie_pk)

        review = form.save(commit=False)
        review.movie = movie
        review.save()

        return HttpResponseRedirect(reverse('movie-details', kwargs={'pk': movie_pk}))
