from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm
from .models import Project
from django.conf import settings


def index(request):
    projects = Project.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']
        context = {'projects': projects, 'message_name': message_name}
        msg = f'{message_name} with email {message_email} said:\n\n'
        msg += message

        if form.is_valid():
            send_mail(
                message_name,
                msg,
                message_email,
                [settings.RECIPIENT_ADDRESS],
            )
    else:
        context = {'projects': projects}
        form = ContactForm()

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
