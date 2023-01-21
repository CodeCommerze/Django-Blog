from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email', 'password1' , 'password2']
        

    def clean_email(self):
        email = self.cleaned_data['email']
        model = self.Meta.model
        user = model.objects.filter(email = email)
        if user.exists():
            raise forms.ValidationError("Email already exists")
       
        return email
    
# class LoginForm(AuthenticationForm):
#     class Meta:
#         model =

    
    

