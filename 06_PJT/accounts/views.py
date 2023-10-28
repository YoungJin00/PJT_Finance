from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUsercreationForm


@require_http_methods(['GET', 'POST'])
def signup(request):
    # 로그인한 사용자가 들어오면 ??
    if request.user.is_authenticated:
        return redirect('boards:index')
    
    # Method기 GET 일때와 POST 일 때
    # POST : 실제로 회원 가입 진행
    if request.method == 'POST':
        form = CustomUsercreationForm(request.POST)
        if form.is_valid():
            # 저장 및 자동 로그인
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        # GET : 회원가입 페이지 보여줘야함
        form = CustomUsercreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
    

@require_http_methods(['GET', 'POST'])
def login(request):
    # 로그인한 사용자가 들어오면 ??
    if request.user.is_authenticated:
        return redirect('boards:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('boards:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

# 세션 데이터를 삭제 > POST 요청
@require_POST
def logout(request):
    # 로그인 안된 사용자가 요청을 보내면 ?
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('boards:index')    

@require_http_methods(['GET'])
def profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    boards = user.board.all()
    comments = user.comment.all()
    followers = user.followers.all()
    context = {
        'boards': boards,
        'comments': comments,
        'user': user,
        'followers': followers
    }
    return render(request, 'accounts/profile.html', context)


@require_http_methods(["POST"])
def follow(request, user_pk):
    person = get_user_model().objects.get(pk=user_pk)
    # 자기 자신은 팔로우 할 수 없음
    if person != request.user:
        # 이미 팔로우 한 유저라면 삭제
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        # 새로 팔로우하는 유저라면 추가
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.pk)