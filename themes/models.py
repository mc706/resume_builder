from django.db import models
from django.contrib.auth.models import User


class Template(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    template = models.TextField(blank=True)
    styles = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
