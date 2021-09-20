from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=500, unique=True)
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("projects")


class TeamLeader (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, default='tl name')
    ssdc_number = models.CharField(max_length=100, default='tl ssdc number')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    date_joined = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("team-leader-profile")


class Agent (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, default='agent name')
    ssdc_number = models.CharField(max_length=100, default='agent ssdc number')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    date_joined = models.DateField(default=timezone.now)
   

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("agent-profile")

STATUS_CHOICES = (
    ("Paid", "Paid"),
    ("Payment Pending", "Payment Pending"),
    ("Not Paid", "Not Paid"),
)

class Invoice(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    isp_name = models.CharField(max_length=100, default='isp name')
    monthly_subscription = models.IntegerField(default='monthly subscription')
    invoice_file = models.FileField(upload_to="invoices/", null=True, blank=True)
    due_date = models.DateField(default=timezone.now)
    approved = models.BooleanField(default=False)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="Payment Pending")
    date_submitted = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.agent) + " Invoice"

    def get_absolute_url(self):
        return reverse("agent-invoices")

    def invoice_approved(self):
        if self.approved:
            return "Yes"
        else: return "No"



