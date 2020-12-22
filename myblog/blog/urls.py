from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('posts',views.Postview.as_view(),name='posts'),
    path('article/<int:pk>',views.Articleview.as_view(),name='article'),
    path('add_post',views.Addpostview.as_view(),name='addpost'),
    path('article/edit/<int:pk>',views.Editview.as_view(),name='editpost'),
]
