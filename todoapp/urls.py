from django.contrib import admin
from django.urls import path, include
from .views import todoappView, addTodoView, deleteTodoView, changeStatus, filterByStatus

urlpatterns = [
    path('todoapp/', todoappView),
    path('addTodoItem/',addTodoView), 
    path('deleteTodoItem/<int:i>/', deleteTodoView), 
    path('changeStatus/<int:i>/', changeStatus), 
    path('filterByStatus/', filterByStatus),
]
