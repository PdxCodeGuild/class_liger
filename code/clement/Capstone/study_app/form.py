from django import forms
from . models import Project, Resource, FlashCard
from django.contrib.auth.models import User



#=================== Creating Project from models=============
class ProjectForm(forms.ModelForm):
    is_finished = forms.BooleanField()
    class Meta:
        model = Project
        fields = ['title', 'description', 'due_date', 'is_finished']

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control'}),
            'due_date' :forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
           
        }
        
#=================== Creating Resources from models=============

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'author', 'price', 'resources_type', 'date_published', 'url']
      
        widgets={
            'name':forms.TextInput(attrs={'class': 'form-control'}),  
            'author':forms.TextInput(attrs={'class': 'form-control'}),  
            'price' :forms.TextInput(attrs={'class': 'form-control'}), 
            'resources_type':forms.TextInput(attrs={'class': 'form-control'}), 
            'url':forms.TextInput(attrs={'class': 'form-control'}), 
            'date_published' :forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                        
        }
# ==============Create a form to create Flashcards for a project=============
class FlashCardForm(forms.ModelForm):
    class Meta:
        model = FlashCard

        fields = ['question', 'answer']

        # widgets={
        #     'question':forms.CharField(attrs={'class': 'form-control'}),
        #     'answer':forms.CharField(attrs={'class': 'form-control'}),

        # }



# ==============Create a RegisterForm  for Registrations =============
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        

        widgets = {
            'username':forms.TextInput(attrs={'class': 'form-control'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class DictionaryForm(forms.Form):
    text = forms.CharField(max_length=100, label="Please enter your world: ")


   