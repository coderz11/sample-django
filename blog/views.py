from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Blog

def hello(request):
    return render(request, 'hello.html', {'message': 'Hello World'})

@login_required
def list(request):
    blog_list = Blog.objects.all()
    return render(request, 'list.html', {'blog_list': blog_list})

@login_required
def detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'detail.html', {'blog': blog})

@login_required
def create(request):
    if request.method == 'POST':
        blog = Blog(title=request.POST.get('title'), content=request.POST.get('content'))
        blog.save()
        return redirect('list')
    else:
        return render(request, 'create.html') 

@login_required
def update(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.content = request.POST.get('content')
        blog.save()
        return redirect('list')
    return render(request,'update.html', {'blog':blog})

@login_required
def delete(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('list')
    return render(request, 'delete.html', {'blog':blog})
