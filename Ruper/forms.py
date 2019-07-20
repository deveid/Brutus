from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ShoppingItem,ShoppingList
#from django import

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    
    def __init__(self, *args, **kwargs):
        """ To remove help_text from regisrer form"""
        super(UserCreationForm,self).__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].help_text=None

    class meta:
        model= User
        fields=('email')

    def save(self,commit=True):
        user=super(RegisterForm,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        if commit==True:
            user.save()
        return user

class LoginForm(forms.Form):
    username=forms.CharField(label="Username", required=True)
    password=forms.CharField(label="Password", max_length=50,widget=forms.PasswordInput)


