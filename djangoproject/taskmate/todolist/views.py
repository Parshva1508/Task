from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist.models import Tasklist
from todolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    context = {
        'index_text' : "Welcome to Taskmate page"
    }
    return render(request, 'home.html',context)

def todolist(request):
    if request.method =="POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,("New Task Added"))
        return redirect('todolist')
          
    else: 
        all_tasks= Tasklist.objects.all()
        paginator = Paginator(all_tasks, 10)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

def deletetask(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

def edittask(request, task_id):
    if request.method =="POST":
        task = Tasklist.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task Edited!"))
        return redirect('todolist')
          
    else: 
        task_obj= Tasklist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})

def completetask(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done = True
    task.save()

    return redirect('todolist')

def pendingtask(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done = False
    task.save()

    return redirect('todolist')


