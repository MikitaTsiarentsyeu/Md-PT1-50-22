from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Author, Post
from .forms import PostForm
from datetime import datetime

# Create your views here.
def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')

def request(request):
    return render(request,'request.html')


def success(request):
    return render(request,'success.html')    


def posts(request):
    posts = Post.objects.all()[::-1]

    return render(request,'posts.html',{'posts':posts})


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = Author.objects.all()[0]
            post.issued = datetime.now()
         

            post.save()
            form.save_m2m()

            return redirect('success')
    else:        

        form = PostForm()
    return render(request, 'request.html',{'form':form})