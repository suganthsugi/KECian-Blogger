from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name="home"),
    path('newpost', views.newpost, name="newpost"),
    path('blog/<slug:slug>/', views.viewpost, name="viewpost"),
    path('my-private-post', views.allmyprivatepost, name="allmyprivatepost"),
    path('my-public-post', views.allmypublicpost, name="allmypublicpost"),
    path('make-public-private/<slug:slug>', views.makepublicprivate, name="makepublicprivate"),
    path('delete-post/<slug:slug>', views.deletePost, name="deletepost"),
    path('search/', views.search, name="search"),
]
