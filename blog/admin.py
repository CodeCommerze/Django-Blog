from django.contrib import admin

from .models import *
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name",]}
admin.site.register(Blog , BlogAdmin)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name",]}
admin.site.register(Category ,CategoryAdmin )
class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name",]}
admin.site.register(Tags , TagsAdmin)

admin.site.register(Comment)
admin.site.register(Replay)