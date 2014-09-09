from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Resume(models.Model):
    """
    Resume model
    """
    title = models.CharField(max_length=100)

    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    csz = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50)

    account = models.ForeignKey(User, related_name='resumes')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.account.username + '-' + self.title

    class Meta:
        verbose_name = 'resume'
        verbose_name_plural = 'resumes'


class Section(models.Model):
    """
    Section
    """
    resume = models.ForeignKey(Resume, related_name='sections')
    title = models.CharField(max_length=100)
    html_class = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Section, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.resume + '(' + self.title + ')'

    class Meta:
        verbose_name = 'section'
        verbose_name_plural = 'sections'


class Entry(models.Model):
    """
    Entry
    """
    section = models.ForeignKey(Section, related_name='entries')
    title = models.CharField(max_length=100, blank=True)
    subtitle = models.CharField(max_length=100, blank=True)
    date_start = models.CharField(max_length=50, blank=True)
    date_finish = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=750, blank=True)

    def __unicode__(self):
        return self.section + '['+self.title+']'

    class Meta:
        verbose_name = 'entry'
        verbose_name_plural = 'entries'
