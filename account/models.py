from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from account.email import send_email_user
import uuid
# all database table class are here 

class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='profile_user')
    image  = models.ImageField(verbose_name="Profile Picture" , upload_to="user/profile")
    first_name = models.CharField(max_length=255 , blank=True, null=True, verbose_name="First Name")
    last_name = models.CharField(max_length=255 , blank=True, null=True , verbose_name="Last Name")
    phone_number = models.CharField(max_length=255 , blank=True, null=True , verbose_name="Phone Number")
    verify_token = models.CharField(max_length=255 , blank=True, null=True, verbose_name=" Id Verify Token")
    reset_token = models.CharField(max_length=255 , blank=True , null=True, verbose_name="Password Reset Token")
    is_active = models.BooleanField(default=False, verbose_name="Id Activated")
    joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
        
    def get_profile_picture(self):
            url = ''
            try:
                url=self.image.url
            except:
                url = '/static/assets/images/default.jpg'
            return url





# for autometic creating user profile and send verify msg to the user email address
@receiver(post_save , sender = User)
def create_profile(sender,instance , created ,  **kwargs):
    if created:
        profile = Profile.objects.create(user = instance , verify_token =str(uuid.uuid4()))
        profile.save()
        send_email_user(instance.email , profile.verify_token )







