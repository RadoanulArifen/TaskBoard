from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from .models import Task

# Create your views here.

def task_list(request):
    tasks = Task.objects.order_by('-created_at')  # Fetch tasks ordered by creation date

    if request.method == 'POST':
        title = request.POST.get('title')  # Get the title from the form submission
        if title:
            Task.objects.create(title=title)  # Create a new task with the provided title
            return redirect('tasks:list')   # Redirect to the task list after creating a new task

    return render(request, 'tasks/task_list.html', {'tasks': tasks})  # Render the task list template with the tasks context


def toggle_complete(request,task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('tasks:list')

def delete(request,task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks:list')