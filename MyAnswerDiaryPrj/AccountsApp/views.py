from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        username = request.POST["user_id"]
        password = request.POST["user_pw"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('main')


def signup(request):
    if request.method == 'POST':
        errMsg = {}
        if User.objects.filter(username=request.POST['user_id']).exists():
            return render(request, 'bad_signup_1.html')
        if request.POST['user_pw'] == request.POST['user_pw_repeat']:
            new_user = User.objects.create_user(username=request.POST['user_id'], password=request.POST['user_pw'], first_name=request.POST['user_nickname'])
            auth.login(request, new_user)
            return redirect('main')
        else:
            return render(request, 'bad_signup_2.html')
    return render(request, 'signup.html')