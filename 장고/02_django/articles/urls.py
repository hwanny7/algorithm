from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),

    # 게시글 생성
    path('create/', views.create, name='create'),

    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),

    # 게시글 수정
    path('<int:pk>/update/', views.update, name='update'),

]
