from django.shortcuts import render
from .models import Blog

def hello(request):
    return render(request, 'hello.html', {'message': 'Hello World'})

def list(request):
    blog_list = Blog.objects.all()
    return render(request, 'list.html', {'blog_list': blog_list})

def detail(request):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'detail.html', {'blog': blog})