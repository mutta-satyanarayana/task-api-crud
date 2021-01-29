from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.tasks_list, name = 'tasks_list'),
    path('detail/<str:pk>', views.task_detail, name = 'task_detail'),
    path('create/', views.task_create, name = 'task_create'),
    path('update/<str:pk>', views.task_update, name = 'task_update'),
    path('delete/<str:pk>', views.task_delete, name = 'task_delete'),

]