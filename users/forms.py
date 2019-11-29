from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    DESIGNATION = (
        ('Undergrad', 'Undergrad'),
        ('Grad Student', 'Grad Student'),
        ('Alumni', 'Alumni'),
        ('Not a student', 'Not a student'),
    )
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    student_designation = forms.ChoiceField(widget=forms.Select, choices=DESIGNATION)
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'student_designation')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'student_designation')