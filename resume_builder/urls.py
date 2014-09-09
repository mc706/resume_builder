from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^api/', include('resume_builder.api-urls')),

    url(r'^admin/', include(admin.site.urls)),
)
