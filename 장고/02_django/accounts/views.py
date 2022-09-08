from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm, 
    # UserCreationForm,     # 이거 대신 custom한 usercreationfrom 을 사용한다
)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash                    #비밀번호 바뀌면 변경된 비밀번호에 맞춰서 session을 다시 클라이언트에 보내는 함수
from . forms import CustomUserCreationForm, CustomUserChangeForm            # 장고의 기본 user 정보가 아닌, 내가 custom 한 것을 사용해야 오류가 나지 않는다.


def login(request):
    if request.user.is_authenticated:                        #이미 로그인 되어 있으면 login 페이지를 보여줄 필요가 없음
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)     # 유효성 검사
        if form.is_valid():                                  #유효성 검사를 통과하면 id와 password 가 있다는 뜻
            auth_login(request, form.get_user())
            return redirect('articles:index')

    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')
# Create your views here.

def signup(request):                # 장고 기본 유저로 되어 있는 것을 바꿔줘야 한다. error: Manager isn't available; 'auth.User' has been swapped for 'accounts.User'
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

# POST 요청 / 로그인 사용자만 가능
def delete(request):
    if request.method == 'POST':
        request.user.delete()           #request 안에 있는 user 인스턴스를 삭제, table에 있는 record는 사라진다.
        auth_logout(request)            #먼저 로그아웃 하고 delete를 하면 어떤 user 정보를 지워야 할지 모르기 때문에 삭제부터 하고 로그아웃 / 로그아웃을 위해서는 user id 등이 필요한데, delete를 해도 이런 데이터는 남아있다.
        return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)        #request.POST는 새로운 데이터
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)

def change_password(request):               #비밀번호 변경을 하면 자동으로 로그아웃이 된다.
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/change_password.html', context)

