from django.urls import path
from blog.views import *

urlpatterns = [
    path("",BlogView.as_view() , name='index'),
    path("blog" , BlogListView.as_view() , name="blog list"),
    path("blog/<str:slug>", BlogDetailsView.as_view() , name='blog_details'),
    path('category/<str:slug>', CategoryFilterView.as_view() , name='category_filter'),
    path('tags/<str:slug>', TagsFilterView.as_view() , name='tags_filter'),
    path('search' , blogSearchView.as_view() , name='blog_search'),
    path('replay/<str:blog_slug>/<str:comment_id>', ReplayView.as_view() , name='replay'),
    path('blog_like/<str:pk>', likeBLog, name='blog_like'),
 

]
