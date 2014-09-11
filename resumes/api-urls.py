from django.conf.urls import patterns, url

urlpatterns = patterns('resumes.api',
    url(r'(?P<resume_slug>[-\w]+)/sections/(?P<section_slug>[-\w]+)/entries/(?P<entry_slug>[-\w]+)/$', 'section_entry', name="section_entry"),
    url(r'(?P<resume_slug>[-\w]+)/sections/(?P<section_slug>[-\w]+)/entries/$', 'list_section_entries', name="list_section_entries"),
    url(r'(?P<resume_slug>[-\w]+)/sections/(?P<section_slug>[-\w]+)/$', 'resume_section', name="list_resume_sections"),
    url(r'(?P<resume_slug>[-\w]+)/sections/$', 'list_resume_sections', name="list_resume_sections"),
    url(r'(?P<resume_slug>[-\w]+)/$', 'resume', name="resume"),
    url(r'$', 'list_resumes', name="list_resumes"),
)