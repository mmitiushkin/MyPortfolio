from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def works(request):
    return render(request, 'mainapp/works.html')


def work_details(request):
    return render(request, 'mainapp/work_detail.html')



