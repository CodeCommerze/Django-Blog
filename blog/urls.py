from django.urls import path
from blog.views import *

urlpatterns = [
    path("",BlogView.as_view() , name='index'),
    path("blog" , BlogListView.as_view() , name="blog list"),
    path("blog/<str:slug>", BlogDetailsView.as_view() , name='blog_details'),
    path("login" , UserLoginView.as_view() , name="user_login"),

]
