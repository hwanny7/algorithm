
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe       #데코레이트 달다가 말았음
from django.contrib.auth.decorators import login_required       #로그인 여부 확인

# Create your views here.
@require_safe
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@login_required     #로그인 한 사람만 create
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()           # article.pk를 전달하기 위해 form이 만든 instance를 article 변수에 담는다.
            # title = request.POST.get('title')
            # content = request.POST.get('content')
            # article = Article(title=title, content=content)
            # article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()        #GET 요청일 경우 form을 반환해서 서식에 작성할 수 있게 한다
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

require_safe        #safe는 GET과 같음. 공식문서에서 GET 대신 safe를 권장함
def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)

@login_required
def update(request, pk):        # edit.html 과 detail.html 에 article.pk 를 요구하는 url이 있기 때문에 article도 넘겨줘야 한다.
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)      #업데이트를 위해 원래 instance를 가져온다.
        if form.is_valid():
            form.save()
            # title = request.POST.get('title')
            # content = request.POST.get('content')
            # article = Article(title=title, content=content)
            # article.save()
        return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)