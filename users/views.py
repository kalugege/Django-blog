from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import UserRegisterForm,EditForm 
from django.contrib.messages.views import SuccessMessageMixin 




class UserView(SuccessMessageMixin,generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_message = 'Your are logge!'
    
    def form_valid(self, form):
        
        form.save()
        
        username = self.request.POST['username']
        password = self.request.POST['password1']
       
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect('/')

class EditView(SuccessMessageMixin, generic.UpdateView):
    form_class = EditForm
    template_name = 'registration/edit-profile.html'
    success_url = reverse_lazy('home')
    success_message = 'Your profile is updated!'
   
    def get_object(self):
        return self.request.user
