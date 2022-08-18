from re import M
from django.db import models
from django.forms import DateTimeField
from django.conf import settings

# Create your models here.

class Diary(models.Model):
    id = models.AutoField(primary_key=True) # pk
    title = models.CharField(max_length = 50) # 제목
    content = models.TextField() #내용
    hashTag = models.CharField(max_length = 20) #해시태그
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete =models.CASCADE) #작성자 
    created_at = models.DateTimeField(auto_now=True) #생성일자
    
    def __str__(self):
        return self.title

class Question365(models.Model):
    question = models.TextField(max_length=60) # 질문
    category = models.CharField(max_length=10) # 카테고리
    num = models.IntegerField() # 질문 숫자

    def __str__(self):
        return self.question

class Answer365(models.Model):
    id = models.AutoField(primary_key=True) # pk
    answer = models.TextField(max_length = 200) # 답변
    created_at = models.DateTimeField(auto_now=True) #생성일자
    question = models.ForeignKey(Question365, on_delete=models.CASCADE) #fk(질문)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete =models.CASCADE) #작성자 
    
    def __str__(self):
        return self.answer