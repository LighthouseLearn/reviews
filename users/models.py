from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    DESIGNATION = (
        ('Undergrad', 'Undergrad'),
        ('Grad Student', 'Grad Student'),
        ('Alumni', 'Alumni'),
        ('Not a student', 'Not a student'),
    )
    age = models.PositiveIntegerField(default=0)
    student_designation = models.CharField(max_length=20, choices=DESIGNATION, null=True, default="None")