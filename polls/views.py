from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'mysite/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()


    context = {
            'form': TaskForm(),
    }
    return render(request, 'mysite/create.html', context)


