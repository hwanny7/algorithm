from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create', views.create, name = 'create'),
    path('<int:pk>/delete', views.delete, name = 'delete'),
    path('<int:pk>', views.verify, name = 'verify'),
]