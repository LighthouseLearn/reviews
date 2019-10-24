from django.db import models
from django.conf import settings
from django.urls import reverse
import numpy as np

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=255,unique=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board,related_name='companies')
    starter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='companies',
    )
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company_detail', args=[str(self.id)])

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    STAY = (
        ('less than 6 months', 'less than 6 months'),
        ('6 months', '6 months'),
        ('10 months', '10 months'),
        ('12 months', '12 months'),
        ('More than 1 year', 'More than 1 year'),
    )
    YES_NO = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    SECURITY = (
        ('100%', '100%'),
        ('75%', '75%'),
        ('50%', '50%'),
        ('25%', '25%'),
        ('0%', '0%'),
        ('Still waiting', 'Still waiting'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODE, null=True, related_name='+')
   
    
    company = models.ForeignKey(Company, related_name='reviews')
    address = models.CharField(max_length=200, blank=False, default="")
    move_in_condition = models.CharField(max_length=5,choices=RATING_CHOICES)
    length_of_stay = models.CharField(max_length=20, choices=STAY, blank=False)

    #Landlord Interaction

    treatment = models.CharField(max_length=5, choices=RATING_CHOICES, blank=False, default ="3")
    response_speed = models.CharField(max_length=5, choices=RATING_CHOICES, blank=False, default ="3")
    maintenance_quality = models.CharField(max_length=5, choices=RATING_CHOICES, blank=False, default ="3")

    security_return = models.CharField(max_length=5, choices=SECURITY, blank=False, default ="1")
    #put text "ignore if still waiting"
    fair = models.CharField(choice=YES_NO, max_length=5, blank=False, default="1")
    recommend = models.CharField(choice=YES_NO, max_length=5, blank=False, default="1")

    additional_comments = models.TextField(max_length=4000)