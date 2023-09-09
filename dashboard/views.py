
from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views import generic
from website.models import Contact, Blogs
from django.http import JsonResponse
from .forms import AddForm
from django.urls import reverse_lazy
from django.utils import timezone

class DashboardView(generic.ListView):
    model= Contact
    template_name = 'dashboard/contacts.html'
    context_object_name = 'contacts'

    def get_queryset(self):
        return Contact.objects.order_by("id")
    
    # def post(self,request, *args, **kwargs):
    #     ids = self.request.POST.get("ids", "")
    #     ids = ids.split()
    #     Contact.objects.filter(id__in=ids).delete()
    #     return JsonResponse({"status": "ok"}, status=204)

    # def get_context_data(self,*args, **kwargs):
    #     context = super().get_context_data(*args,**kwargs)
    #     c=(self.kwargs["pk"])
    #     Contact.objects.get(id=c).delete()
    #     return context
    
class ReceivedMessage(generic.DetailView):
    model = Contact
    template_name= "dashboard/received_message.html"
    context_object_name= "message"

    

def delete_info(request, pk):
    Contact.objects.get(id=pk).delete()
    return redirect("dashboard:message")

class BlogView(generic.ListView):
    model= Blogs
    template_name = 'dashboard/blog.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blogs.objects.order_by("id")
    
class Blogcontent(generic.DetailView):
    model = Blogs
    template_name= "dashboard/blog_content.html"
    context_object_name= "content"



def add_blog(request):
    
    if request.method == "POST":
        
        form = AddForm(request.POST)
        
        if form.is_valid():
           print(form.cleaned_data)
           b = Blogs()
           b.title = form.cleaned_data["title"]
           b.author= form.cleaned_data['author']
           b.updated_on = timezone.now()
           b.content= form.cleaned_data['content']
           b.status= form.cleaned_data['status']
           b.created_on= timezone.now()
           b.save()
           return redirect("dashboard:blog_view")
           

    
    else:
        form = AddForm()

    return render(request, "dashboard/add_blog.html", {"form": form})

def delete_blog(request, pk):
	queryset = Blogs.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect("dashboard:blog_view")
	return render(request, 'dashboard/delete_blog_items.html')

def update_blog(request, pk):
    queryset= Blogs.objects.get(id=pk)
    if request.method == "POST":
        
        form = AddForm(request.POST)
        
        if form.is_valid():
           b = Blogs.objects.get(id=pk)
           b.title = form.cleaned_data["title"]
           b.author= form.cleaned_data['author']
           b.updated_on = timezone.now()
           b.content= form.cleaned_data['content']
           b.status= form.cleaned_data['status']
           b.created_on= timezone.now()
           b.save()
           return redirect("dashboard:blog_view")
    else:
        form = AddForm()

    return render(request, "dashboard/update_blog.html", {"form": form})