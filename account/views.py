from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView , LogoutView
from account.form import RegisterForm  
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class RegisterView(CreateView,SuccessMessageMixin ):
  form_class = RegisterForm 
  template_name = "components/authentication/signup.html"
  success_url = reverse_lazy("login")
  success_message = "We have send a Email confirmation to your email address"
  

  def get(self , request, *args, **kwargs):
    if request.user.is_authenticated:
      return  redirect('index')
    return super(RegisterView , self).get(request, *args, **kwargs)
  
  def form_valid(self, form) :
    user = form.cleaned_data["email"]
    print(user)
    messages.success(self.request ,"An Email send To Your Email")
    return super().form_valid(form)  
   

class LoginUserView(LoginView):
  template_name = "components/authentication/login.html"
  redirect_authenticated_user = True
  
