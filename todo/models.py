from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    # str타입을 저장하는 최대길이의 default값을 줘야한다.
    deadline = models.DateField()

# db.column으로 설정했던 것을 model로 설정한다.
# 메소드가 달라졌다고 생각하면 된다. 
# 실제로 데이터 베이스 모델을 설정할 땐 모델을 성
# python manage.py makemigrations
# flask db migrate와 같이 설계도를 만들어준다. 

# python manage.py migrate
# 해당명령어로 실제 db에 반영을 해준다. 
# 어떻게 생겼는지 어떻게 살필까요?

# python manage.py createsuperuser
# 아이디 비밀번호 하고 

    def __str__(self):
        return self.title
        
# view - CRUD 로직
