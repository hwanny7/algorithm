from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
# Create your views here.

@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    
    return render(request, 'todo/index.html', context)


def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                form = form.save(commit = False)
                form.author = request.user
                form.save()
                return redirect('todo:index')
        else:
            form = ArticleForm()
    else:
        return redirect('accounts:login')
    context = {
        'form':form
    }
    return render(request, 'todo/create.html', context)


def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk = pk)
        print(article.author, request.user)
        if request.user == article.author:
            print('hello')
            article.delete()
    
    return redirect('todo:index')

def verify(request, pk):
    article = Article.objects.get(pk= pk)
    article.completed = not article.completed
    article.save()
    return redirect('todo:index')