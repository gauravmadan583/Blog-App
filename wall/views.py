from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'wall/home.html', context)

def about(request):
    return render(request, 'wall/about.html', {'title': 'About'})