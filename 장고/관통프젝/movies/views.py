from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movie = Movie.objects.order_by('pk')
    context = {
        'movies' : movie,
    }
    return render(request, 'movies/index.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/detail.html', context)

def new(request):
    contents = {
        'genres':['action', 'horror', 'comic', 'SF', 'animation']
        }
    return render(request, 'movies/new.html', contents)

def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    movie = Movie(title=title, audience=audience, release_date=release_date, genre=genre, poster_url=poster_url, description=description, score=score)
    movie.save()
    return redirect('movies:detail', movie.pk)

def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    content = {
        'movie':movie,
        'genres':['action', 'horror', 'comic', 'SF', 'animation']
    }
    return render(request, 'movies/edit.html', content)

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.release_date = request.POST.get('release_date')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')
    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.save()
    return redirect('movies:detail', movie.pk)

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')
    
