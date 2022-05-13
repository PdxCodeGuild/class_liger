from dataclasses import field, fields
from . models import BlogPost
from django import forms




class BlogForm(forms.ModelForm):

    class Meta:

        model = BlogPost

        fields = [

            'title',
            'body', 
            'user', 
            'public', 
            # 'date_created', 
            # 'date_edited',
        ]

        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.TextInput(attrs={'class': 'form-control'}),
            'user' : forms.TextInput(attrs={'class': 'form-control'}),
            'public' : forms.TextInput(attrs={'class': 'form-control'}),
            'date_created' : forms.TextInput(attrs={'class': 'form-control'}),
            'date_edited':forms.TextInput(attrs={'class': 'form-control'}),
        }





