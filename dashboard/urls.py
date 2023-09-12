from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

app_name = "dashboard"
urlpatterns = [
    path('',login_required(views.DashboardView.as_view()), name='message'),
    path("message/<int:pk>/", login_required(views.ReceivedMessage.as_view()), name="received_messages"),
    path('<int:pk>/delete/', login_required(views.delete_info),name="delete_messages"),
    path('blog/',login_required(views.BlogView.as_view()), name='blog_view'),
    path("contents/<int:pk>/", login_required(views.Blogcontent.as_view()), name="contents"),
    path("addblog/", login_required(views.add_blog), name="new_blog"),
    path('<str:pk>/delete_items/', login_required(views.delete_blog), name="delete_blog"),
    path('update/<int:pk>' , login_required(views.update_blog), name="update"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]