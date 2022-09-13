from . import views
from django.urls import path

app_name = 'travels'
urlpatterns = [
    path('', views.index , name='index'),
    path('create/', views.create , name='create'),
    path('<int:pk>', views.detail , name='detail'),
]