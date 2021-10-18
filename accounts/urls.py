from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *
# 로그인 후 /accounts/profile 로 이동(기본값)
# 1. profile 페이지 생성 / 2. profile 페이지가 아닌 페이지로 보내기(a. 장고 설정 변경 / b. 웹서버에서 설정)

urlpatterns = [
    path('login', auth_view.LoginView.as_view(), name="login"),
    path('logout', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
    path('register/', register, name='register'),
]