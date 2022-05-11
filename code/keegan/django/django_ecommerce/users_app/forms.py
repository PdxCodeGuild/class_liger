from django import forms
from .models import User

# create a custom form class based on the information in the User model
class UserForm(forms.ModelForm):
    # the Meta class will descrive the data used to create the form
    # this includes the DB Model class, which fields from the model to include
    # and the HTML widgets that should be used for each field
    class Meta:
        # this form is for creating/editing objects from the User model
        model = User

        # include all the model's fields in the form
        # fields = '__all__'
        fields = [
            'first_name',
            'last_name',
        ]

        # customize the HTML widgets for each field
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }


# create a form specifically for registering/logging in users
class UserAuthForm(UserForm):

    # inherit the meta data from the UserForm and override which fields are included
    class Meta(UserForm.Meta):
        fields = ['username', 'password']