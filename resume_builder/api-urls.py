from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^themes/', include('themes.api-urls')),
    url(r'^resumes/', include('resumes.api-urls')),
    url(r'^types/', 'resumes.api.list_sectiontypes'),
)
