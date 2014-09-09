from django.shortcuts import render_to_response, render, RequestContext, HttpResponse, get_object_or_404
from django.http import JsonResponse
from themes.models import Template


def list_templates(request):
    templates = Template.objects.all()
    return JsonResponse(render(request, "api/templates.json", {'templates':templates}))


def template(request, template_slug):
    template = get_object_or_404(Template, slug=template_slug)
    return JsonResponse(render(request, "api/template.json", {'template':template}))


def template_css(request, template_slug):
    template = get_object_or_404(Template, slug=template_slug)
    return HttpResponse(status=200, content_type="text/css", content_type=render(request, "api/theme.css", {'template':template}))