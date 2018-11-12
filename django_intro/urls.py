"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# views.py의 메소드를 사용하기 위해 import 하는 작업
# from 앱이름 import views 파일을 가져와 라는 것이다. 
from app_intro import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('lunch/',views.lunch),
    path('lotto/',views.lotto),
    path('hello/<str:name>',views.hello),
    path('cube/<int:number>',views.cube),
    path('todos/', include('todo.urls')),
    ]

    # include를 통해 다른 app인 todo에 urls라는 파일 안에 포함되어있다고 알려준다 
    
    
    # ''사이에 아무것도 없는 것 루트 index 페이지를 의미한다. 
    # 장고에서는 외부에 있는 메소드를 가져와서 사용한다고 말해줘야한다. (''랑 ,method로 가볍게 설정해놓는다 객체지향같은느낌)
    # def에 해당되는 코드들은 app.py가 아니라 --> views.py에 작성할 것이다. 
    # 리스트 형태로 , 로 끝내준다(list안에 넣어놨기때문이당)
    # '블라블라/'로 링크를 넣어야한다.
    # url 페이지에 뒤에 받을 인자를 해준다. 'hello/<str:name>'
    # <str:name> 이런 부분을 인자커버터라고 부른다. 
    # str 사용 가능 / int 사용 가능 / slug 사용 가능
    # str 어떤 것이 들어오던지 str 허용
    # int 0또는 양의정수
    # slug 문자 또는 숫자 하이픈 _ - 모두 받는다.
    # default값은 항상 str이다. 
