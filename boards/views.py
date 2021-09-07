from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from .models import Projects
# Create your views here.

def home(request):
    boards = Projects.objects.all()
    return render(request, 'home.html', {'boards': boards})

def project(request, pk):
    project = get_object_or_404(Projects, pk=pk)
    return render(request, 'project.html', {'project': project})
