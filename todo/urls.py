from django.urls import path
from . import views
# 이거는 현재 폴더 안에 있는 view 파일 추가 
# todo라는 폴더안에 있는 views에 접근을 할 것이다. 

urlpatterns = [
    path('',views.index),    
    path('new/', views.new), # CRUD 로직에서 Create는 new와 create라는 두 개로 나눴ㄷ.\
    # new라는 url은 html을 보여준다. post요청 일대, get 요청일 떄
    # form을 주고 입력을 받기 위한 것
    # 실제로 저장하는 로직은 create에 있을 거싱다.
    path('create/',views.create)
]