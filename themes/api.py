import json
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from themes.models import Template, Style
from themes.forms import TemplateForm, StyleForm


def list_templates(request):
    if request.method == "GET":
        templates = Template.objects.all()
        return JsonResponse(render(request, "api/templates.json", {'templates': templates}))
    elif request.method == "POST":
        if request.user.is_authenticated():
            data = json.loads(request.body)
            form = TemplateForm(data)
            if form.is_valid():
                new_template = form.save(commit=False)
                new_template.create = request.user
                new_template.save()
                return JsonResponse(status=201,
                                    data=render(request, "api/template.json", {'template': new_template}))
            else:
                return JsonResponse(form.errors)
        else:
            return HttpResponse(status=403)


def template(request, template_slug):
    template = get_object_or_404(Template, slug=template_slug)
    if request.method == "GET":
        return JsonResponse(render(request, "api/template.json", {'template': template}))
    elif request.method == "PUT":
        if request.user.is_authenticated() and request.user == template.creator:
            data = json.loads(request.body)
            form = TemplateForm(data)
            if form.is_valid():
                new_template = form.save(commit=False)
                new_template.creator = request.user
                new_template.save()
                return JsonResponse(status=204,
                                    data=render(request, "api/template.json", {'template': new_template}))
            else:
                return JsonResponse(form.errors)
        else:
            return HttpResponse(status=403)
    elif request.method == "DELETE":
        if request.user.is_authenticated() and request.user == template.creator:
            template.delete()
            HttpResponse(status=202)
        else:
            return HttpResponse(status=403)
    else:
        return HttpResponse(status=403)


def template_css(request, template_slug):
    if request.method == "GET":
        template = get_object_or_404(Template, slug=template_slug)
        return HttpResponse(status=200, content_type="text/css",
                            content_type=render(request, "api/theme.css.template", {'template': template}))
    else:
        return HttpResponse(status=403)


def list_template_styles(request, template_slug):
    template = get_object_or_404(Template, slug=template_slug)
    if request.method == "GET":
        styles = template.styles.all()
        return JsonResponse(styles)
    elif request.method == "POST":
        data = json.loads(request.body)
        form = StyleForm(data)
        if form.is_valid():
            new_style = form.save(commit=False)
            new_style.template = template
            new_style.save()
            return JsonResponse(status=204,
                                    data=render(request, "api/style.json", {'style': new_style}))
        else:
            return JsonResponse(form.errors)
    else:
        return HttpResponse(status=403)


def template_style(request, template_slug, section_id):
    template = get_object_or_404(Template, slug=template_slug)
    style = get_object_or_404(Style, template=template, section__id=section_id)
    if request.method == "GET":
        return JsonResponse(render(request, "api/style.json", {'style': style}))
    elif request.method == "PUT":
        if request.user.is_authenticated() and request.user == template.creator:
            data = json.loads(request.body)
            form = StyleForm(data)
            if form.is_valid():
                new_style = form.save(commit=False)
                new_style.template = template
                new_style.save()
                return JsonResponse(status=204,
                                    data=render(request, "api/style.json", {'style': new_style}))
            else:
                return JsonResponse(form.errors)
        else:
            return HttpResponse(status=405)
    elif request.method == "DELETE":
        if request.user.is_authenticated() and request.user == template.creator:
            style.delete()
            HttpResponse(status=202)
        else:
            return HttpResponse(status=403)

