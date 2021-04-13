from io import StringIO
from django.shortcuts import render
from .models import Post
#from django.views.generic import ListView



def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_list.html', {'posts': posts})