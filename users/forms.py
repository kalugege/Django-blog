from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name' , 'last_name', 'password1', 'password2')

    def __init__(self,*args,**kwargs):
        super(UserRegisterForm,self).__init__(*args,**kwargs)  


class EditForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name' , 'last_name']

         
