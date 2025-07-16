from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

class Profile(models.Model):
    user = models.OneToOneField('auth.user',on_delete=models.CASCADE)
    phone = models.CharField(max_length=15,blank=True,null=True)
    dob = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username

