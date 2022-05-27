from django import forms

# import the pic model to use to create the form
from .models import Pic

class PicForm(forms.ModelForm):
    class Meta:
        model = Pic

        # limit the fields to just the image and the caption,
        # not the user or date_created
        fields = ['image', 'caption']

        # widgets are the HTML elements that are rendered for each field
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'caption': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'style': 'resize: none; white-space: pre-wrap'
                }
            )
        }