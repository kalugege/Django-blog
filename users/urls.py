from django.urls import path
from .views import UserView,EditView
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('register/' , UserView.as_view()  ,name ='register'),
    path('edit-profile/' , EditView.as_view()  ,name ='edit'),
    path('password/',PasswordChangeView.as_view(template_name = 'registration/password.html', success_url='/'),name='password'),



]