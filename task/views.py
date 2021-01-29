from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
# task operations
# tasks list, task detail, task update, task delete, create task

@api_view(['GET'])
def tasks_list(request):
    tasks = Task.objects.all()
    serializers  = TaskSerializer(tasks, many = True)
    return Response(serializers.data)


@api_view(['GET'])
def task_detail(request, pk):
    #task = Task.objects.get(id = pk)
    task = get_object_or_404(Task, id = pk)
    serializer = TaskSerializer(instance= task, many = False)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    print("\n\naccessed")
    new_task = TaskSerializer(data = request.data)
    if new_task.is_valid():
        new_task.save()
    return Response(new_task.data)


@api_view(['POST'])
def task_update(request, pk):
    update_task = Task.objects.get(id = pk)
    serializer = TaskSerializer(instance= update_task, data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE','GET'])
def task_delete(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return Response("Task Successfully Deleted...")