from django.contrib import admin
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','title','audience','release_date','genre','score','description')

admin.site.register(Movie, MovieAdmin)