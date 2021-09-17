from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
# class User(AbstractUser):
#     is_agent = models.BooleanField(default=False)
#     is_teamleader = models.BooleanField(default=False)

class Agent (models.Model):
    name = models.CharField(max_length=150, default='agent name')
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    ssdc_number = models.CharField(max_length=100, default='agent ssdc number')
    isp_name = models.CharField(max_length=100, default='isp name')
    monthly_subscription = models.IntegerField(default='monthly subscription')
    due_date = models.DateField(default='due date')
    approved = models.BooleanField(default='true or false')


class TeamLeader (models.Model):
    name = models.CharField(max_length=150, default='tl name')
    ssdc_number = models.CharField(max_length=100, default='tl ssdc number')
    project = models.CharField(max_length=60, default='project name')
