from django.db import models

# Create your models here.

class Article(models.Model):     #models 모듈 안에 model을 상속 받아야 한다. 테이블 이름은 appname_classname
    # primary-key ==> 따로 정의 하지 않으면, id라는 필드가 자동으로 생성된다.
    # Article의 인스턴스들을 같은 데이터 베이스에 처리하도록 작동한다.
    # record를 조회하는 것은 각각의 인스턴스들의 값을 가져오는 것이다.
    # 필드 정의 ==> 이름 = 필드타입()
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now = True)

    def __str__(self):          #class 안에 정의해야지 메소드로 작동할 수 있다.
        return f'{self.title} - {self.content}'