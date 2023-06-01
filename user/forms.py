from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

INPUT_CLASSES='w-full px-6 py-4 rounded-xl'
class LoginForm(forms.Form):
    username=forms.CharField(max_length=60, widget=forms.TextInput(attrs={
        'placeholder':'Enter your username ',
        'class':'w-full px-6 py-4 rounded-xl',
    }))
    password=forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={
        'placeholder':'Enter your password',
        'class':'w-full py-4 px-6 rounded-xl '
    }))

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'w-full py-4 px-6 rounded-xl'
    }))   
    email=forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Your email address',
        'class':'w-full py-4 px-6 rounded-xl'
    })) 
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class':'w-full py-4 px-6 rounded-xl'
    })) 
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repeat your password',
        'class':'w-full py-4 px-6 rounded-xl'
    })) 
