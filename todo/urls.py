from django.urls import path

from .views import home, todo_list

urlpatterns = [
    path("", home, name="home"),
    path("todos/", todo_list, name="todo_list"),
]
