# 앱의 라우팅만 담당하는 파일
from django.urls import path
from polls import views

urlpatterns = [
    path('', views.index, name='index'),
]
