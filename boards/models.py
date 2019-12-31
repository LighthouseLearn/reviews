from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models import Avg, F, Sum


# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_reviews_count(self):
        return Review.objects.filter(company__board=self) .count()
    
    def get_last_review(self):
        return Review.objects.filter(company__board=self) .order_by('created_at') .last()

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    #bio = models.TextField(max_length=4000)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete = models.CASCADE, related_name='companies')
    starter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='companies',
    )
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company_detail', args=[str(self.id)])
    
    def get_recent_reviews(self):
        return self.reviews.order_by('-created_at')

    def get_last_ten_reviews(self):
        return self.reviews.order_by('-created_at')[:10]

    def get_avg(self):
        return self.reviews.annotate(
            overall_rating = Sum(
                F('move_in_condition') + 
                F('treatment') + 
                F('response_speed') +
                F('maintenance_quality')
            )/4).aggregate(
                Avg('overall_rating'), 
                Avg('move_in_condition'),
                Avg('treatment'),
                Avg('response_speed'),
                Avg('maintenance_quality')
            )

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
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='reviews')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null=True, related_name='+')
    company = models.ForeignKey(Company, on_delete = models.CASCADE, related_name='reviews')
    address = models.CharField(max_length=200, blank=False, default="")
    length_of_stay = models.CharField(max_length=20, choices=STAY, blank=False, default="None")
 
    move_in_condition = models.IntegerField(choices=RATING_CHOICES, blank=False, default=5)
    #Landlord Interaction
    treatment = models.IntegerField(choices=RATING_CHOICES, blank=False, default =5)
    response_speed = models.IntegerField(choices=RATING_CHOICES, blank=False, default =5)
    maintenance_quality = models.IntegerField(choices=RATING_CHOICES, blank=False, default =5)    

    security_deposit_returned = models.CharField(max_length=13, choices=SECURITY, blank=False, default ="None")
    #put text "ignore if still waiting"
    is_this_a_fair_amount = models.CharField(max_length=5, choices=YES_NO, blank=False, default="1")
    would_you_recommend = models.CharField(max_length=5, choices=YES_NO, blank=False, default="1")
    additional_comments = models.TextField(max_length=4000)

    def __str__(self):
        return self.address
       #Apartment Condition
   # move_in_condition = models.CharField(max_length=5,choices=RATING_CHOICES, blank=False, default='5')
    #Landlord Interaction
   # treatment = models.CharField(max_length=5, choices=RATING_CHOICES, blank=False, default ="5")
   # response_speed = models.CharField(max_length=5, choices=RATING_CHOICES, blank=False, default ="5")
  #  maintenance_quality = models.CharField(max_length=5, choices=RATING_CHOICES, blank=False, default ="5")
    


