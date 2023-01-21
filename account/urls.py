from django.urls import path
from account import views
from django.contrib.auth.views import LogoutView
# all the routes of accunt
urlpatterns = [
    path('register',views.RegisterView.as_view() , name="register"),
    path('login' ,views.LoginUserView.as_view() , name="login" ),
    path('logout', LogoutView.as_view() , name="logout")
]
