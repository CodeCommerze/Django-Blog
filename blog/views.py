from django.shortcuts import render
from django.views.generic import ListView , DetailView , TemplateView 
from django.contrib.auth.views import LoginView
# Models
from blog.models import *


class BlogView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = Blog.objects.all()[:4]
        context["categorys"] = Category.objects.all()[:4]
        print(self.kwargs)
        return context
    


class BlogListView(ListView):
    model = Blog
    paginate_by = 6
    context_object_name = "blogs"
    template_name = 'blog.html'
   

class BlogDetailsView(DetailView):
    model=Blog
    template_name = "blog_details.html"
    context_object_name = "blog"


class UserLoginView(LoginView):
    template_name = 'contact.html'
    success_url = "index"




           