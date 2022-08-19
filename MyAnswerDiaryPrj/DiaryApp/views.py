from ast import keyword
from distutils.log import Log
from this import d
from tkinter import Y
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from .models import Answer365, Diary, Question365
from django.db.models import Q
from datetime import date, timedelta
import datetime

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
    return render(request, 'index.html')

def mood_graph(request):

    # 현재 날짜(년, 월, 일)
    todayYear = date.today().year
    todayMonth = datetime.date.today().month
    todayDay = datetime.date.today().day

    startYear = todayYear -1
    startMonth = todayMonth
    startDay = todayDay

    endYear = todayYear
    endMonth = todayMonth
    endDay = todayDay

    #해시태그 개수
    joy = 0
    anger = 0
    depression = 0
    pleasure = 0

    #현재 날짜 ~ 1년전 날짜 사이의 일기 데이터 조회 (아무것도 입력 하지 않았을 때)
    todayDiarys2 = Diary.objects.filter(created_at__range = [date.today()-timedelta(days=365),date.today()]).values().all()

    print(todayDiarys2)
    for todayDiary in todayDiarys2 :
        if todayDiary.get('hashTag') == "기쁨" :
            joy = joy + 1
        
        if todayDiary.get('hashTag') == "분노" :
            anger= anger + 1

        if todayDiary.get('hashTag') == "우울" :
            depression = depression + 1
        
        if todayDiary.get('hashTag') == "즐거움" :
            pleasure = pleasure + 1

    # 퍼센트 구하기
    total = joy+anger+depression+pleasure
    joyPercent = joy / total * 100
    angerPercent = anger / total * 100
    depressionPercent = depression / total * 100
    pleasurePercent = pleasure / total * 100

    if(request.method =="GET") :
        if request.user.is_authenticated :
            #현재 날짜 ~ 1년전 날짜 사이의 일기 데이터 조회 (아무것도 입력 하지 않았을 때)
            todayDiarys2 = Diary.objects.filter(created_at__range = [date.today()-timedelta(days=365),date.today()]).values().all()

            for todayDiary in todayDiarys2 :
                if todayDiary.get('hashTag') == "기쁨" :
                    joy = joy + 1
        
                if todayDiary.get('hashTag') == "분노" :
                    anger= anger + 1

                if todayDiary.get('hashTag') == "우울" :
                    depression = depression + 1
        
                if todayDiary.get('hashTag') == "즐거움" :
                    pleasure = pleasure + 1

            # 퍼센트 구하기
            total = joy+anger+depression+pleasure
            joyPercent = joy / total * 100
            angerPercent = anger / total * 100
            depressionPercent = depression / total * 100
            pleasurePercent = pleasure / total * 100


        return render(request, 'mood_graph.html', {'joyPercent':joyPercent, 'angerPercent':angerPercent, 'depressionPercent':depressionPercent, 'pleasurePercent':pleasurePercent, 
        'startYear':startYear, 'startMonth':startMonth , 'startDay': startDay, 'endYear' : endYear, 'endMonth' : endMonth, 'endDay': endDay })
            
    # 특정 기간 입력 후 검색 결과       
    if(request.method == "POST") : 
        if request.user.is_authenticated :
            startYear = int(request.POST['startYear'])
            startMonth = int(request.POST['startMonth'])
            startDay = int(request.POST['startDay'])

            endYear = int(request.POST['endYear'])
            endMonth = int(request.POST['endMonth'])
            endDay = int(request.POST['endDay'])

            start_date = datetime.date(startYear,startMonth,startDay)
            end_date = datetime.date(endYear,endMonth,endDay)

            searchDiarys = Diary.objects.filter(created_at__range=(start_date,end_date)).values().all()
            print("검색 일기",searchDiarys)

            for searchDiary in searchDiarys :
                if searchDiary.get('hashTag') == "기쁨" :
                    joy = joy + 1
        
                if searchDiary.get('hashTag') == "분노" :
                    anger= anger + 1

                if searchDiary.get('hashTag') == "우울" :
                    depression = depression + 1
        
                if searchDiary.get('hashTag') == "즐거움" :
                    pleasure = pleasure + 1

            # 퍼센트 구하기
            total = joy+anger+depression+pleasure
            joyPercent = joy / total * 100
            angerPercent = anger / total * 100
            depressionPercent = depression / total * 100
            pleasurePercent = pleasure / total * 100

        return render(request, 'mood_graph.html', {'joyPercent':joyPercent, 'angerPercent':angerPercent, 'depressionPercent':depressionPercent, 'pleasurePercent':pleasurePercent, 
        'startYear':startYear, 'startMonth':startMonth , 'startDay': startDay, 'endYear' : endYear, 'endMonth' : endMonth, 'endDay': endDay })

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

def qna(request):

    # 현재 날짜(년, 월, 일)
    todayYear = date.today().year
    todayMonth = datetime.date.today().month
    todayDay = datetime.date.today().day

    nowday = datetime.datetime.now().day # 현재 일(day)
    if (nowday%5 == 0):
        nownum = 5
    else:
        nownum = nowday % 5
    ques = Question365.objects.filter(num=nownum)

    # 오늘 날짜에 작성된 카테고리 리스트
    answers = Answer365.objects.all()
    count = 0
    answerYear = []
    answerMonth = []
    answerDay = []
    yearGap = []

    for answer in answers:
        print("user", answer.user)
        print("오늘", todayMonth,"월", todayDay,"일")
        print("month : ", answer.created_at.month)
        print("day : ", answer.created_at.day)
        answerYear.append(answer.created_at.year)
        answerMonth.append(answer.created_at.month)
        answerDay.append(answer.created_at.day)
        if ((answer.created_at.month == todayMonth) and (answer.created_at.day == 18)):
            count += 1
                
    #     #pk가 없어서 질문 문자열 값을 통해 question 객체 조회
    #     question = Question365.objects.get(question = request.POST['que'])
    #     print(question)
    #     # if request.user.is_authenticated and question is not "":
    #     for i in range(count):
    #         today_answers = answers.order_by('-created_at').filter(
    #             Q(created_at__month=todayMonth), 
    #             Q(created_at__day=18),
    #             Q(question=question),
    #             user=request.user
    #         ).distinct()
    #         yearGap.append(todayYear - answerYear[i])
    #         print("today_answers", today_answers);
    
    if request.method == 'GET':
        print("get요청임")

        if request.user.is_authenticated:
            for i in range(count):
                print("todayDay",todayDay)
                print("day",answerDay[i])
                today_answers = answers.order_by('-created_at').filter(
                    Q(created_at__month=todayMonth), 
                    Q(created_at__day=todayDay),
                    user=request.user,
                ).distinct()      
                print("today_answers", today_answers)
                print("ques", ques)
                print("answers", answers)
                return render(request, 'qna.html', {'ques':ques , 'today_answers':today_answers, 'answers': answers, 'todayYear': todayYear, 'todayMonth' : todayMonth, 'todayDay' : todayDay, 'yearGap':yearGap}) #'today_answers':today_answers, 
        # return render(request, 'main.html')  
        # # 오늘 날짜에 작성된 카테고리 리스트
        # answers = Answer365.objects.all()
        # count = 0
        # answerYear = []
        # answerMonth = []
        # answerDay = []
        # yearGap = []

        # for answer in answers:
        #     print("user", answer.user)
        #     print("오늘", todayMonth,"월", todayDay,"일")
        #     print("month : ", answer.created_at.month)
        #     print("day : ", answer.created_at.day)
        #     answerYear.append(answer.created_at.year)
        #     answerMonth.append(answer.created_at.month)
        #     answerDay.append(answer.created_at.day)
        #     if ((answer.created_at.month == todayMonth) and (answer.created_at.day == 18)):
        #         count += 1
                    
        # if request.user.is_authenticated:
        #         for i in range(count):
        #             today_answers = answers.order_by('-created_at').filter(
        #                 Q(created_at__month=todayMonth), 
        #                 Q(created_at__day=18),
        #                 user=request.user
        #             ).distinct()
        #             yearGap.append(todayYear - answerYear[i])
        #             print("today_answers", today_answers);
            

            
            
        
    if request.method == 'POST':
        
        if request.user.is_authenticated:
            answer = Answer365()
            answer.answer = request.POST['answer']
            answer.created_at = timezone.now()

            #pk가 없어서 질문 문자열 값을 통해 question 객체 조회
            question = Question365.objects.get(question = request.POST['que'])
            # print(question)
            #question을 fk로 저장
            answer.question = question
            answer.user = request.user
            answer.save()
            yearGapCount = 0;
            for answer in answers:
                # print("user", answer.user)
                # print("오늘", todayMonth,"월", todayDay,"일")
                # print("month : ", answer.created_at.month)
                # print("day : ", answer.created_at.day)
                answerYear.append(answer.created_at.year)
                answerMonth.append(answer.created_at.month)
                answerDay.append(answer.created_at.day - 1)
                count += 1
                # if ((answer.created_at.month == todayMonth) and (answer.created_at.day == 18)):
                #     count += 1
                # for i in range(yearGapCount):
                    # yearGap.append(todayYear - answerYear[i])
                # print(todayDay, "==", answer.created_at.day)
                if ((request.user.is_authenticated) and (question == answer.question)):
                    for i in range(count):
                        today_answers = answers.order_by('-created_at').filter(
                            Q(created_at__month=todayMonth), 
                            Q(created_at__day=todayDay),
                            Q(question=answer.question),
                            user=request.user,
                        ).distinct()
                        yearGap.append(todayYear - answerYear[i])
                        # print("today_answers", today_answers);
                        return render(request, 'qna.html', {'ques':ques , 'todayYear': todayYear, 'todayMonth' : todayMonth, 'todayDay' : todayDay, 'today_answers':today_answers, 'yearGap':yearGap, 'answerDay':answerDay})
            
        else :
            return redirect('main') #로그인 되어있지 않으면 main으로 redirect
    


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
