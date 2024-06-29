from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    EMPLOYEE = 'employee'
    HR = 'hr'
    ADMIN = 'admin'
    ROLE_CHOICES = [
        (EMPLOYEE, 'Employee'),
        (HR, 'HR'),
        (ADMIN, 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=EMPLOYEE)

class Grievance(models.Model):
    TYPE_CHOICES = [
        ('Workplace', 'Workplace'),
        ('Harassment', 'Harassment'),
        ('Discrimination', 'Discrimination'),
        ('Other', 'Other'),
    ]
    SEVERITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grievances')
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField()
    department = models.CharField(max_length=100)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    grievance = models.ForeignKey(Grievance, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
