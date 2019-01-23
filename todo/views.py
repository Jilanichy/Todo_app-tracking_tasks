from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    if request.method == "POST":
        form = TodoForm(request.POST or None)
        if form.is_valid():
            form.save()
            tasks = Todo.objects.all()
            messages.success(request, ('Item Has Been Added to the Task List Successfully!'))
            return render(request, 'todo/home.html', {'tasks':tasks})

    tasks = Todo.objects.all()
    return render(request, 'todo/home.html', {'tasks':tasks})


def delete(request, task_id):
    task = Todo.objects.get(pk=task_id)
    task.delete()
    messages.success(request, ('Item Has Been Deleted!'))
    return redirect('home')

def cross_off(request, task_id):
    task = Todo.objects.get(pk=task_id)
    task.task_finished = True
    task.save()
    return redirect('home')

def uncross(request, task_id):
    task = Todo.objects.get(pk=task_id)
    task.task_finished = False
    task.save()
    return redirect('home')

def edit(request, task_id):
    if request.method == "POST":
        task = Todo.objects.get(pk=task_id)

        form = TodoForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, ('Item Has Been Edited Successfully!'))
            return redirect('home')

    task = Todo.objects.get(pk=task_id)
    return render(request, 'todo/edit.html', {'task':task})
