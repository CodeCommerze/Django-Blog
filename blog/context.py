from blog.models import Blog , Category,Tags

def SidebarView(request):
    blog = Blog.objects.all().order_by('-created')
    category = Category.objects.all().order_by('-created')
    tag = Tags.objects.all().order_by('-created')
    
    context = {
        'blogs': blog,
        'categories': category,
        "tags":tag
    }
    return context