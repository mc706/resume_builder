from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from resumes.models import SectionType

class Template(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True)
    global_styles = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Template, self).save(*args, **kwargs)

    def get_css_url(self):
        return reverse("template_css", args=(self.slug,))


class Style(models.Model):
    template = models.ForeignKey(Template, related_name='styles')
    section = models.ForeignKey(SectionType, related_name='styles')
    styles = models.TextField(blank=True)

    def __unicode__(self):
        return "{0.template.name}({0.section.name})".format(self)

    def get_styles(self):
        return "div.{0.section.html_class} { {0.styles} }".format(self)

    class Meta:
        unique_together = ('template', 'section')
