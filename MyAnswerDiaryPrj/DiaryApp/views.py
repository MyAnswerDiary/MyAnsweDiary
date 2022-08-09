from distutils.log import Log
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from .models import Diary
from django.db.models import Q

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


def searchpage(request):
    return render(request, 'searchpage.html')

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
    if diary_detail.user == request.user:
        return render(request, 'detail.html', {'diary_detail':diary_detail})
    else:
        return render(request, 'bad_detail.html') # 사용자가 다른 유저의 본문을 보지 못하게 함