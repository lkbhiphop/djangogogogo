from django.shortcuts import render
import random
# Create your views here.
def index(request):
    return render(request, 'index.html')
# request는 없었고, render가 아니라 render_template을 했었는데 그게 바뀐것뿐 구조는 같다. 
def lunch(request):
    menu_list = ['20층','김까','사골집']
    pick = random.choice(menu_list)
    return render(request,'lunch.html',{'pick':pick})
    # request, html문서, 딕셔너리 타입으로 넣어준다.
def lotto(request):
    number = random.sample(list(range(1,46)),6)
    return render(request,'lotto.html',{'lotto':number})
    # ''안에있는것이 html에서 쓰일 변수의 이름이므니다.
def hello(request, name):
    return render(request, 'hello.html',{'name':name})
    
def cube(request, number):
    cube = number ** 3
    return render(request,'cube.html',{'cube':cube})