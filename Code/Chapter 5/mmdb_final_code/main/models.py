from __future__ import unicode_literals

from django.db import models
from django.utils.translation import get_language


class MovieDetails(models.Model):
    title = models.CharField(max_length=500)
    title_fr = models.CharField(max_length=500)

    description = models.TextField()
    description_fr = models.TextField()

    stars = models.PositiveSmallIntegerField()

    def get_title(self):
        return self._get_translated_field('title')

    def get_description(self):
        return self._get_translated_field('description')

    def _get_translated_field(self, field_name):
        original_field_name = field_name

        lang_code = get_language()
        
        if lang_code != 'en':
            field_name = '{}_{}'.format(field_name, lang_code)
        field_value = getattr(self, field_name)
                
        if field_value:
            return field_value
        else:
            return getattr(self, original_field_name)

    def __str__(self):
        return self.title


class MovieReview(models.Model):
    movie = models.ForeignKey(MovieDetails, related_name='reviews')
    user_name = models.CharField(max_length=100)
    review = models.TextField()
