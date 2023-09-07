from django.urls import path
from .views import index, HomePageView, BlogDetailView
app_name = 'website'
urlpatterns = [
    path('', HomePageView.as_view(), name = "index"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name = "blog_view"),
]