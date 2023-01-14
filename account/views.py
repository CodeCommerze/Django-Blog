from django.shortcuts import render

# all account vies are here
def login_user(request):
  return render(request , "components/authentication/login.html")