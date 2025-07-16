from django.contrib import admin
from .models import Task,Profile
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','is_active')
    search_fields = ('title',)
    list_filter = ('is_active','created_at')
    ordering = ('-created_at',)
    