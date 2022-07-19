import email
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Author, Post
from .forms import AddPost, AddPostModelForm
from datetime import datetime

def home(request):
    return render(request, 'home.html')

def posts(request):

    posts = Post.objects.all()
    viewed_posts = request.session.get("viewed_posts", {})
    print(viewed_posts)
    
    return render(request, 'posts.html', {'posts': posts, 'viewed_posts':viewed_posts})

def post(request, post_id):

    viewed_posts = request.session.get("viewed_posts", {})
    viewed_posts[post_id] = int(post_id)
    request.session["viewed_posts"] = viewed_posts

    post = Post.objects.get(id=post_id)
    return render(request, 'post.html', {'post':post, 'viewed_posts':viewed_posts})

def add_post(request):

    if request.method == "POST":
        form = AddPost(request.POST, request.FILES)

        if form.is_valid():
            post = Post()
            post.author = Author.objects.get(email=request.user.email)
            post.issued = datetime.now()
            post.title = form.cleaned_data['title']
            post.subtitle = form.cleaned_data['subtitle']
            post.content = form.cleaned_data['content']
            post.image = form.cleaned_data['image']
            post.post_type = form.cleaned_data['post_type']

            post.save()

            return redirect('posts')
    else:
        form = AddPost()

    return render(request, 'add_post.html', {'form':form})

def add_post_model_form(request):
    if request.method == "POST":
        form = AddPostModelForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = Author.objects.get(email=request.user.email)
            post.issued = datetime.now()

            post.save()
            form.save_m2m()

            return redirect('posts')
    else:
        form = AddPostModelForm()

    return render(request, 'add_post.html', {'form':form})