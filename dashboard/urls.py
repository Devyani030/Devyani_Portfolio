from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path('',views.DashboardView.as_view(), name='message'),
    path("message/<int:pk>/", views.ReceivedMessage.as_view(), name="received_messages"),
    path('<int:pk>/delete/', views.delete_info,name="delete_messages"),
    path('blog/',views.BlogView.as_view(), name='blog_view'),
    path("contents/<int:pk>/", views.Blogcontent.as_view(), name="contents"),
    path("addblog/", views.add_blog, name="new_blog"),
    path('<str:pk>/delete_items/', views.delete_blog, name="delete_blog"),
    path('update/<int:pk>' , views.update_blog, name="update"),
]