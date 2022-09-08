from ssl import HAS_TLSv1_1
from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')
    content = {'articles':articles}
    return render(request, 'articles/index.html', content)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:index')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    content = {
        'article':article
        }
    return render(request, 'articles/detail.html', content)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    content = {
        'article':article
    }

    return render(request, 'articles/edit.html', content)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()              
    return redirect('articles:detail', pk)