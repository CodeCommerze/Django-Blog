from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255 )
    slug = models.SlugField(max_length=255 , unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Tags(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    

class Blog(models.Model):
    user = models.ForeignKey(User,related_name="author" ,verbose_name="Author" , on_delete=models.CASCADE)
    image= models.ImageField(upload_to='blog/banner' , verbose_name="Banner")
    Category = models.ForeignKey(Category , related_name="blog_category" , on_delete=models.CASCADE)
    name = models.CharField(max_length=255 , verbose_name="Blog Title",help_text="Eneter The Blog Title Here")
    slug = models.SlugField(max_length=255 , null=True , blank=True , unique=True)
    view = models.ManyToManyField(User , related_name="user_view", blank=True)
    description = models.TextField(max_length=255)
    likes  = models.ManyToManyField(User,blank=True )
    Tags = models.ManyToManyField(Tags , blank=True)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('-created',)
    def get_absolute_url(self):
        return reverse("blog_details", kwargs={"slug": self.slug})
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    

class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="user_comment")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE , related_name="blog_comment")
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.comment

class Replay(models.Model):
    user = models.ForeignKey(User, related_name="replay_user" , on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment , verbose_name= "Comment", related_name='replay_comment' , on_delete=models.CASCADE)
    text = models.CharField(max_length=255 , verbose_name="Replay")
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username


