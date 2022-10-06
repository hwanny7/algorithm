from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from django.views.decorators.http import require_http_methods, require_POST, require_safe

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'either/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form = form.save()
        return redirect('either:detail', form.pk)
    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'either/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk = pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article':article,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'either/detail.html', context)

@require_POST
def comment_create(request, pk):
    article = Article.objects.get(pk = pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        form = form.save(commit = False)
        form.article = article
        form.save()

    return redirect('either:detail', article.pk)
