from ast import keyword
from distutils.log import Log
from this import d
from tkinter import Y
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from .models import Diary
from django.db.models import Q
import datetime
from datetime import date

def main(request):
    todayYear = date.today().year
    todayMonth = datetime.date.today().month
    todayDay = datetime.date.today().day
    diaryYear = []
    diaryMonth = []
    diaryDay = []
    yearGap = []
    diarys = Diary.objects.all()
    count = 0;
    
    for diary in diarys:
        diaryYear.append(diary.created_at.year)
        diaryMonth.append(diary.created_at.month)
        diaryDay.append(diary.created_at.day)
        count += 1  
    # return render(request, 'main.html', {'todayYear':todayYear, 'todayMonth':todayMonth, 'todayDay':todayDay})

    if request.user.is_authenticated:
        for i in range(count):
            today_diarys = diarys.order_by('-created_at').filter(
                Q(created_at__month=todayMonth), 
                Q(created_at__day=todayDay),
                user=request.user
            ).distinct()
            yearGap.append(todayYear - diaryYear[i])
        return render(request, 'main.html', {'today_diarys':today_diarys, 'todayYear':todayYear, 'todayMonth':todayMonth, 'todayDay':todayDay, 'yearGap':yearGap})
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


def searchpage(request):
    return render(request, 'searchpage.html')

def qa365(request):
    return render(request, 'qa365.html')
    
def mood_graph(request):
    return render(request, 'mood_graph.html')

def search(request):
    if 'kw' in request.GET:
        keyword = request.GET.get('kw')
        diarys = Diary.objects.all().order_by('-created_at').filter(
                Q(title__icontains=keyword) |
                Q(content__icontains=keyword), # Q를 이용해 or 조건을 걸어줌
                user=request.user # 로그인한 사용자의 글만 보이도로 and 조건
            ).distinct() # or 검색시 중복된 글이 나타나는 것을 방지(중복 없애주는 함수)
        return render(request, 'search.html', {'keyword':keyword , 'diarys':diarys})

    else:
        return render(request, 'search.html')

def detail(request, diary_id):
    diary_detail = get_object_or_404(Diary, pk=diary_id)
    diaryYear = []
    diaryMonth = []
    diaryDay = []
    yearGap = []
    count = 0
    diarys = Diary.objects.all()
    for diary in diarys:
        diaryYear.append(diary.created_at.year)
        diaryMonth.append(diary.created_at.month)
        diaryDay.append(diary.created_at.day)
        count += 1

    # detail_day : 상세페이지 메인 일기(클릭한 일기)
    # diaryDay : 상세페이지 리스트 일기(클릭한 일기와 같은 날짜에 쓰여진 일기들)
    if diary_detail.user == request.user:
        detail_at = diarys[diary_id - 1].created_at
        detail_year = diarys[diary_id - 1].created_at.year
        detail_month = diarys[diary_id - 1].created_at.month
        detail_day = diarys[diary_id - 1].created_at.day
        
        for i in range(count):
            detail_diarys = Diary.objects.all().order_by('-created_at').filter(
                    Q(created_at__month=detail_month), 
                    Q(created_at__day=detail_day),
                    ~Q(created_at=detail_at), #클릭한 일기와 같은 글은 제외
                    user=request.user
                ).distinct()
            yearGap.append(diaryYear[i] - detail_year);
        return render(request, 'detail.html', {'diary_detail':diary_detail, 'detail_diarys':detail_diarys, 'yearGap':yearGap})
    else:
        return render(request, 'bad_detail.html')
