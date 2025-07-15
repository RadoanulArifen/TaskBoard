from django.urls import path
from . import views

app_name = "tasks"  # ✅ This must match your namespace in project urls

urlpatterns = [
    path('', views.task_list, name='list'),
    path('toggle/<int:task_id>/',views.toggle_complete , name = 'toggle_complete'),
    path('toggle<int:task_id>/', views.delete,name='delete')
]
