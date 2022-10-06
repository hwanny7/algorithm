from . import views
from django.urls import path

app_name = 'either'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create', views.create, name = 'create'),
    path('<int:pk>', views.detail, name = 'detail'),
    path('<int:pk>/comment', views.comment_create, name = 'comment_create'),
    path('<int:pk>/delete', views.delete, name = 'delete'),
    path('random', views.random_pick, name = 'random'),
    path('<int:pk>/update', views.update, name = 'update'),
]
