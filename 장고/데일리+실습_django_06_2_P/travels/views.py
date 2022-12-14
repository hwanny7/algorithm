from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm



# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' :articles
    }
    return render(request, 'travels/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('travels:detail', article.pk)        #detail로 바꿔야함
    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'travels/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'travels/detail.html', context)