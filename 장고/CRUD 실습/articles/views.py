from django.shortcuts import render, redirect       # render와 redirect import
from .models import Article         #models폴더에서 Article 클래스를 import

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {                     #반환하고 싶은 인스턴스를 딕셔너리 형태로 만든다.
        'articles':articles,
    }
                                        #렌더 함수를 통해 html과 context를 반환한다.
    return render(request, 'articles/index.html', context) 

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')       #title이 없는 경우에는 None을 return
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()                         #저장이 되면 바로 index page에 반영이 된다.
    # return render(request, 'articles/create.html')
    return redirect('articles:detail', article.pk)       #detail 페이지로 돌려 보내기. redirect 함수는 pk를 인자로 받아야 함.

# /articles/<int:pk>/
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):            #원래는 get이 아니라 post로 요청을 보내는 게 맞다.
    # if request.method == 'POST':
    #     article = Article.objects.get(pk=pk)
    #     article.delete()
    #     return redirect('articles:index')
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')      
    article.content = request.POST.get('content')
    article.save()                      #저장까지 해야 데이터 베이스에 반영이 된다.           
    return redirect('articles:detail', article.pk)          #article.pk 를 detail 함수에 넘겨줘야 작동이 된다.


    