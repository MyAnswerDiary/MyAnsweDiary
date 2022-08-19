from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        username = request.POST['form-id']
        password = request.POST['form-pw']
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
        if User.objects.filter(username=request.POST['form-id']).exists():
            return render(request, 'bad_signup_1.html')
        if request.POST['form-pw'] == request.POST['form-repw']:
            new_user = User.objects.create_user(username=request.POST['form-id'], password=request.POST['form-pw'], first_name=request.POST['form-name'])
            auth.login(request, new_user)
            return redirect('main')
        else:
            return render(request, 'bad_signup_2.html')
    return render(request, 'signup.html')