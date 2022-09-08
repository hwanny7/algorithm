from django import forms                #form이랑 모델 form이 들어있는 모듈 import
from .models import Article

class ArticleForm(forms.ModelForm):     #forms 모듈 안에 Form 상속

    # regin = forms.ChoiceField(
    #     choices = [('서울', '서울'), ('대전', '대전')]    #모델에 정의되지 않았기 때문에 요청은 날라오지만 database에 저장되지는 않는다.
    # )
    
    title = forms.ChoiceField(          #form에 자동으로 만들어지는 title의 input type 등을 새로 정의할 수 있다.
        choices = [('서울', '서울'), ('대전', '대전'), ('영동', '영동'), ('옥천', '옥천')],
        # widget= forms.RadioSelect     
    )

    class Meta:
        model = Article                 #Article을 import 해와야함
        fields = '__all__'              #models에 정의된 모든 field를 사용한다.
        # fields = ('titie', 'content',)  #사용하고 싶은 field만 지정할수도 있다.



    # title = forms.CharField(max_length=10)        model form을 사용하지 않고, form만 상속 받았을 때는 일일이 field를 설정해줘야함
    # content = forms.CharField(
    #     label='내용:',
    #     widget=forms.Textarea(
    #         attrs= {
    #             'class': 'my content',
    #         }
    #     ),
    # )