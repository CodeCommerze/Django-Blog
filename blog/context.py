from blog.models import Blog , Category,Tags

def SidebarView(request):
    blog = Blog.objects.all().order_by('-created')[:4]
    category = Category.objects.all().order_by('-created')[:4]
    tag = Tags.objects.all().order_by('-created')[:10]
    
    context = {
        'blogs': blog,
        'categories': category,
        "tags":tag
    }
    return context
    
