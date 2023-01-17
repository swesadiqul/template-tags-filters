from django import forms
from django.forms import ModelForm
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#create forms
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': '6', 'placeholder': 'Your message ...'}),
        }

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]