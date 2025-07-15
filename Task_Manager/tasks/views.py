from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from .models import Task
from django.views.decorators.http import require_POST
# Create your views here.

def task_list(request):
    tasks = Task.objects.order_by('-created_at')  # Fetch tasks ordered by creation date

    if request.method == 'POST':
        title = request.POST.get('title')  # Get the title from the form submission
        if title:
            Task.objects.create(title=title)  # Create a new task with the provided title
            return redirect('tasks:list')   # Redirect to the task list after creating a new task

    return render(request, 'tasks/task_list.html', {'tasks': tasks})  # Render the task list template with the tasks context


@require_POST
def toggle_complete(request,task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('tasks:list')

@require_POST
def delete(request,task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks:list')

#for registration 
def register(request):
    if request.method == 'POST':
        pass
    return render(request, 'tasks/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
    return render(request, 'tasks/login.html')