from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'mainapp/index.html', context)


def works(request):
    return render(request, 'mainapp/works.html')


def work_details(request, pk):
    project = Project.objects.get(pk=pk)
    techs = project.technologies.split(',')
    funcs = project.functions.split(',')

    has_overview = True
    if not project.overview: has_overview = False

    has_funcs = True
    if funcs == ['']: has_funcs = False

    context = {'project': project,
               'techs': techs,
               'funcs': funcs,
               'has_funcs': has_funcs,
               'has_overview': has_overview}
    return render(request, 'mainapp/work_detail.html', context)
