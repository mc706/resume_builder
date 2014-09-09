from django.conf.urls import patterns, url

urlpatterns = patterns('themes.api',
    url(r'(?P<template_slug>[-\w]+)/theme\.css$', 'template_css', name="template_css"),
    url(r'(?P<template_slug>[-\w]+)/$', 'template', name="template"),
    url(r'$', 'list_templates', name="list_templates"),


)