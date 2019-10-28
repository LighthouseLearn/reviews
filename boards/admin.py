from django.contrib import admin

# Register your models here.
from . import models

class ReviewAdmin(admin.ModelAdmin):
    model = models.Review
    list_display = ('company', 'would_you_recommend', 'address', 'response_speed', 'maintenance_quality', 'created_at', 'created_by')
    list_filter = ['company', 'would_you_recommend', 'address', 'response_speed', 'maintenance_quality', 'created_at', 'created_by']
    search_fields = ['company__name']

admin.site.register(models.Board)
admin.site.register(models.Company)
admin.site.register(models.Review, ReviewAdmin)