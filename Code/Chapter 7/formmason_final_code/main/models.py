from __future__ import unicode_literals

from django.db import models

from jsonfield import JSONField


class FormSchema(models.Model):
    title = models.CharField(max_length=100)
    schema = JSONField()

class FormResponse(models.Model):
    form = models.ForeignKey(FormSchema)
    response = JSONField()