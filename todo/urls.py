from django.urls import path

from .views import home, todo_add, todo_delete, todo_list, todo_update

urlpatterns = [
    path("", home, name="home"),
    path("todos/", todo_list, name="todo_list"),
    path("todo/add", todo_add, name="todo_add"),
    path("todo/update/<int:id>", todo_update, name="todo_update"),
    path("todo/delete/<int:id>", todo_delete, name="todo_delete"),
]
