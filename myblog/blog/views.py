from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm

def home(request):
    return render(request,'home.html')

class Postview(ListView):
    model=Post
    template_name="x.html"

class Articleview(DetailView):
    model=Post
    template_name="article.html"

class Addpostview(CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'
    #fields='__all__'

class Editview(UpdateView):
    model=Post
    template_name='edit_post.html'
    fields=['title','author','body']