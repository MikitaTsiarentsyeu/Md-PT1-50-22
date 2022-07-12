from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    return render(request, 'home.html')

def posts(request):

    posts = Post.objects.all()
    
    return render(request, 'posts.html', {'posts': posts})

def post(request, post_id):

    post = Post.objects.get(id=post_id)
    return render(request, 'post.html', {'post':post})