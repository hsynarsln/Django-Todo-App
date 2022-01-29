from django.http import HttpResponse
from django.shortcuts import render

from .models import Todo

# Create your views here.


def home(request):
    return render(request, "todo/home.html")


def todo_list(request):
    todos = Todo.objects.all()
    contex = {
        'todos': todos
    }
    return render(request, "todo/todo_list.html", contex)


def todo_add(request):
    pass


def todo_update(request, id):
    pass


def todo_delete(request, id):
    pass
