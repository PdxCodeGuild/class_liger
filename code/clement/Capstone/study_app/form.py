from django import forms
from . models import Project, Resource
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Creating forms from models
class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'description']


class BookForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'author', 'price', 'resources_type', 'url']

        widgets={
            'name':forms.TextInput(attrs={'class': 'form-control'}),  
            'author':forms.TextInput(attrs={'class': 'form-control'}),  
            'price' :forms.TextInput(attrs={'class': 'form-control'}), 
            'resources_type':forms.TextInput(attrs={'class': 'form-control'}), 
            'url':forms.TextInput(attrs={'class': 'form-control'}), 
            
        }



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        # widgets={
        #     'username':forms.TextInput(attrs={'class': 'form-control'}), 
        #     'password' :forms.PasswordInput(attrs={'class': 'form-control'}),
            # 'password_2':forms.PasswordInput(attrs={'class': 'form-control'}),
        # }

        





   