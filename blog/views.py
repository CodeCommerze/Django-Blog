from django.shortcuts import render , get_object_or_404 ,redirect 
from django.urls import reverse
from django.http import HttpResponse 
from django.views.generic import ListView , DetailView , TemplateView
from django.views.generic.edit import CreateView ,FormView
from django.contrib.auth.views import LoginView
from .forms import CommentForm , ReplayForm 
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
   

class BlogDetailsView(DetailView , ):
    model=Blog
    template_name = "blog_details.html"
    context_object_name = "blog"
    slug_field = 'slug'
    form = CommentForm

    # For geetting context 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context

    # for post request and 
    def post(self, request,  **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
           comment = Comment.objects.create(
                user = request.user ,
                blog = self.get_object(),
                comment = form.cleaned_data['text']
            )
           comment.save()
        return redirect(reverse("blog_details", kwargs={'slug':kwargs['slug']}))

class ReplayView(FormView):
    def post(self, request ,  **kwargs):
        form = ReplayForm(request.POST)
        comment = get_object_or_404(Comment , pk=self.kwargs['comment_id'])
        print(kwargs['comment_id'])
        if form.is_valid():
            user_replay = Replay.objects.create(
                user = request.user,
                comment=comment,
                text = form.cleaned_data.get('text')        
                )
            user_replay.save()
        return redirect(reverse("blog_details", kwargs={'slug':kwargs['blog_slug']}))

        





class CategoryFilterView(BlogListView):
    BlogListView.template_name  = "components/filter/category.html"

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, slug = self.kwargs.get('slug'))
        context['blogs'] = category.blog_category.all()
        return context

class TagsFilterView(BlogListView):
    BlogListView.template_name='components/filter/tags_filter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = get_object_or_404(Tags, slug=self.kwargs.get('slug'))
        context['blogs'] = tags.blog_set.all()
        return context


    






