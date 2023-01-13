from django.urls import path
from account import views
# all the routes of accunt
urlpatterns = [
    path('login' ,views.login_user , name="login_User "  )
]
