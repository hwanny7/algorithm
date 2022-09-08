from django.urls import path
from . import views               #현재 폴더에 있는 views를 import한다. views가 어디에 있는 views인지 표시하기 위해 명시적으로 . 이라는 표현을 쓴다. 


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),        #articles 뒤에 아무것도 없을 경우, index 함수를 실행.
    # 게시글 생성 양식 /articles /new/
    path('new/', views.new, name='new'),
    # 게시글 DB에 반영 /articles/create/
    path('create/', views.create, name='create'),
    # 게시글 상세 조회 / articles/글번호(pk)/
    # path converter (변환할 데이터 파일 / str은 생략 가능)
    # 존재하는 pk 넘버만이 조회가 가능함. 아니면 페이지 오류가 난다.
    path('<int:pk>/', views.detail, name='detail'),
    # 게시글 삭제 /articles/pk/delete/
    path('<int:pk>/delete/', views.delete, name='delete'),
    # 게시글 수정 /articles/pk/edit/
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]