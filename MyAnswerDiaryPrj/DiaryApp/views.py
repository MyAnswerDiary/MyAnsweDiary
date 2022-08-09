
from distutils.log import Log
from django.shortcuts import redirect, render
from django.utils import timezone

from .models import Diary

def main(request):
    return render(request, 'main.html')

def createDiary(request):

    if request.method == 'POST':

        if request.user.is_authenticated:
            diary = Diary()
            diary.title = request.POST['title']
            diary.content = request.POST['content']
            diary.hashTag = request.POST['hashtag']
            diary.user = request.user
            diary.created_at = timezone.now()
            diary.save()
            return redirect('main')
            
        else :
            return redirect('main') #로그인 되어있지 않으면 main으로 redirect
    else: 
        return render(request, 'create_diary.html')
