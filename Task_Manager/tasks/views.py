from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from .models import Task , Profile
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
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
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'tasks/register.html', {'error': 'User already exists'})

        # ✅ Create the User (only with username, email, password)
        user = User.objects.create_user(username=username, password=password, email=email)

        # ✅ Create the Profile (extended info)
        Profile.objects.create(user=user, phone=phone, dob=dob)

        return redirect('tasks:login')  # ensure this URL name exists
    return render(request, 'tasks/register.html')

def login_view(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')  
        password = request.POST.get('password') 
        try:
            profile = Profile.objects.get(phone=phone)
            user = authenticate(username = profile.user.username, password=password)
            
            if user:
                login(request,user)
                return redirect('tasks:list')
        except User.DoesNotExist:
            return render(request,'tasks/login.html',{'error':'User with this phone nu,ber does not exists'})
    
    return render(request, 'tasks/login.html')

def logout_view(request):
    logout(request)
    return redirect('tasks:login')

def changepass(request):
    if request.method == 'POST':
        new = request.POST.get('new_password')
        confirm = request.POST.get('confirm_password')
        if new == confirm:
            request.user.set_password(new)
            request.user.save()
            update_session_auth_hash(request,request.user)
            return redirect('tasks:list')
        else:
            return render(request,'tasks/change_password.html', {'error': 'Passwords do not match'})
    return render(request, 'tasks/change_password.html')