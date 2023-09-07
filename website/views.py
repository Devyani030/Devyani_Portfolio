from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import Contact , Blogs
from django.views import generic

def index(request):
    return render(request, 'website/index.html',)

class HomePageView(CreateView):
    template_name = 'website/index.html'

    model = Contact
    fields = '__all__'

    def get_success_url(self):
        return '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"]= "Devayni's Portfolio"
        context["blogs"]= Blogs.objects.filter(status=1).order_by("id")
        return context

class BlogDetailView(generic.DetailView):
    model = Blogs
    template_name= "website/blog_contents.html"
    context_object_name= "blog"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"]= Blogs.objects.filter(status=1).order_by("id")
        return context
