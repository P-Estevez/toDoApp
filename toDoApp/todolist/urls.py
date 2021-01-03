from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodoItem, name='add'),
    path('completed/<todoId>', views.completedTodo, name='completed'),
    path('deleteCompleted', views.deleteCompleted, name='deleteCompleted'),
    path('deleteAll', views.deleteAll, name='deleteAll')
]
