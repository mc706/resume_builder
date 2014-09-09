from django.db import models
from django.contrib.auth.models import User
from resumes.models import SectionType

class Template(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Style(models.Model):
    template = models.ForeignKey(Template, related_name='styles')
    section = models.ForeignKey(SectionType, related_name='styles')
    styles = models.TextField()

    def __unicode__(self):
        return "{0.template.name}({0.section.name})"

    class Meta:
        unique_together = ('template', 'section')
