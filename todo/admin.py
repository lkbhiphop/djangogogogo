from django.contrib import admin
from todo.models import Todo
# 이말은 todo models에 Todo를 가져온다.
# Register your models here.
admin.site.register(Todo)
