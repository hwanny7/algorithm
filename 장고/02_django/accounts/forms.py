from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm): #UserCreationForm을 다 상속 받아서 오버라이딩을 통해 custom 한다.

    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)           #수정하고 싶은 field만 적기, migrations 0001 에서 봐도 되고, 공식문서에서 봐도 됨