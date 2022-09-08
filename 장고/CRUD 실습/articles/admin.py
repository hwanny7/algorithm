from django.contrib import admin
from .models import Article     #현재 폴더에 있는 models(모듈 파일)에서 Article을 import
                                #현재 폴더에서 불러오는 것이지만 명시적으로 . 을 써준다.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'updated_at',)       #admin 페이지에 보여주고 싶은 field를 입력한다.

# Register your models here.
admin.site.register(Article, ArticleAdmin)       #admin 사이트에서 관리하고 싶은 테이블을 등록한다. articleadmin도 같이 반환한다.