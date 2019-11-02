from django import forms
from .models import Company, Review

class NewCompanyForm(forms.ModelForm):
    #additional_comments = forms.CharField(widget=forms.Textarea(), max_length=4000)
    #address = forms.CharField(max_length=200)
    #move_in_condition = forms.CharField(max_length=5)

    class Meta:
        model = Company
        fields = ['name']
        # 'length_of_stay', 'treatment', 'response_speed', 'maintenance_quality', 'security_deposit_returned', 'is_this_a_fair_amount', 'would_you_recommend', 

class ReviewForm(forms.ModelForm):
   
    class Meta:
        model = Review
        fields = ['address', 'length_of_stay', 'move_in_condition', 'treatment', 'response_speed', 'maintenance_quality', 'security_deposit_returned', 'is_this_a_fair_amount', 'would_you_recommend', 'additional_comments']