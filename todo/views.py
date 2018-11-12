from django.shortcuts import render
from todo.models import Todo

# Create your views here.
def index(request):
    #우리가 원하는 모델 넣어주기
    # flask에서 Todo.query.all# 데이터 베이스 읽어버리기
    todos = Todo.objects.all()# Todo 모든 object 불러오기 
    return render(request,'todo/index.html',{'todos':todos})
    
# 같은 이름의 html이 있을 수 잇으니 이름 나눠서해야한다. 
def new(request):
    return render(request,'todo/new.html')