import json
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from resumes.models import Resume, SectionType, Section, Entry
from resumes.forms import ResumeForm, SectionForm, EntryForm


def list_sectiontypes(request):
    types = SectionType.objects.all()
    return JsonResponse(json.dumps(types))


@login_required(login_url='/login/')
def list_resumes(request):
    if request.method == "GET":
        resumes = Resume.objects.all()
        return JsonResponse(render(request, "api/resumes.json", {'resumes': resumes}))
    elif request.method == "POST":
        data = json.loads(request.body)
        form = ResumeForm(data)
        if form.is_valid():
            new_resume = form.save(commit=False)
            new_resume.create = request.user
            new_resume.save()
            return JsonResponse(status=201,
                                data=render(request, "api/resume.json", {'resume': new_resume}))
        else:
            return JsonResponse(form.errors)


@login_required(login_url='/login/')
def resume(request, resume_slug):
    resume = get_object_or_404(Resume, slug=resume_slug, account=request.user)
    if request.method == "GET":
        return JsonResponse(render(request, "api/full_resume.json", {'resume': resume}))
    elif request.method == "PUT":
        data = json.loads(request.body)
        form = ResumeForm(data)
        if form.is_valid():
            new_resume = form.save(commit=False)
            new_resume.account = request.user
            new_resume.save()
            return JsonResponse(status=204,
                                data=render(request, "api/resume.json", {'resume': new_resume}))
        else:
                return JsonResponse(form.errors)
    elif request.method == "DELETE":
        resume.delete()
        HttpResponse(status=202)
    else:
        return HttpResponse(status=403)


@login_required(login_url='/login/')
def list_resume_sections(request, resume_slug):
    resume = get_object_or_404(Resume, slug=resume_slug, account=request.user)
    if request.method == "GET":
        sections = resume.sections.all()
        return JsonResponse(render(request, "api/sections.json", {'sections': sections}))
    elif request.method == "POST":
        data = json.loads(request.body)
        form = SectionForm(data)
        if form.is_valid():
            new_section = form.save(commit=False)
            new_section.resume = resume
            new_section.save()
            return JsonResponse(status=201,
                                data=render(request, "api/section.json", {'section': new_section}))
        else:
            return JsonResponse(form.errors)


@login_required(login_url='/login/')
def resume_section(request, resume_slug, section_slug):
    resume = get_object_or_404(Resume, slug=resume_slug, account=request.user)
    section = get_object_or_404(Section, resume=resume, slug=section_slug)
    if request.method == "GET":
        return JsonResponse(render(request, "api/section.json", {'section': section}))
    elif request.method == "PUT":
        data = json.loads(request.body)
        form = SectionForm(data)
        if form.is_valid():
            new_section = form.save(commit=False)
            new_section.resume = resume
            new_section.save()
            return JsonResponse(status=204,
                                data=render(request, "api/section.json", {'section': new_section}))
        else:
                return JsonResponse(form.errors)
    elif request.method == "DELETE":
        section.delete()
        HttpResponse(status=202)
    else:
        return HttpResponse(status=403)


@login_required(login_url='/login/')
def list_section_entries(request, resume_slug, section_slug):
    resume = get_object_or_404(Resume, slug=resume_slug, account=request.user)
    section = get_object_or_404(Section, resume=resume, slug=section_slug)
    if request.method == "GET":
        entries = section.entires.all()
        return JsonResponse(render(request, "api/entries.json", {'entires': entries}))
    elif request.method == "POST":
        data = json.loads(request.body)
        form = EntryForm(data)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.section = section
            new_entry.save()
            return JsonResponse(status=201,
                                data=render(request, "api/entry.json", {'entry': new_entry}))
        else:
            return JsonResponse(form.errors)


@login_required(login_url='/login/')
def section_entry(request, resume_slug, section_slug, entry_slug):
    resume = get_object_or_404(Resume, slug=resume_slug, account=request.user)
    section = get_object_or_404(Section, resume=resume, slug=section_slug)
    entry = get_object_or_404(Entry, section=section, slug=entry_slug)
    if request.method == "GET":
        return JsonResponse(render(request, "api/entry.json", {'entry': entry}))
    elif request.method == "PUT":
        data = json.loads(request.body)
        form = EntryForm(data)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.resume = resume
            new_entry.save()
            return JsonResponse(status=204,
                                data=render(request, "api/entry.json", {'entry': new_entry}))
        else:
                return JsonResponse(form.errors)
    elif request.method == "DELETE":
        entry.delete()
        HttpResponse(status=202)
    else:
        return HttpResponse(status=403)