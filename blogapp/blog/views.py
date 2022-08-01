from django.shortcuts import render

from .models import Post, Blog


def index(request):
    posts = Blog.objects.all()
    return render(request, 'index.html', {'blog': posts})


def setpost(request):
    pset = Post.objects.all()
    return render(request, 'publish.html', {'publish': pset})


def post_de(request, id):
    posts = Blog.objects.get(id=id)
    return render(request, 'viewpost.html', {'post': posts})
