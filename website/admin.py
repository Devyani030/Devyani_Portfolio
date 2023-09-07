from django.contrib import admin

# Register your models here.
from .models import Contact,Blogs

class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title','status', 'created_on')
    list_filter=("status",)
    search_fields=["title", 'content']
    

admin.site.register(Contact)
admin.site.register(Blogs ,BlogsAdmin )