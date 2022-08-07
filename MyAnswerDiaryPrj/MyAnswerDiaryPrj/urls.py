from unicodedata import name
from django.contrib import admin
from django.urls import path
from DiaryApp import views
from AccountsApp import views as ac_views
from DiaryApp import views as diary_views

urlpatterns = [
    path("admin/", admin.site.urls),

    path('', views.main, name='main'),
    path('login/', ac_views.login, name='login'),
    path('logout/', ac_views.logout, name='logout'),
    path('signup/', ac_views.signup, name='signup'),
    path('create_diary/',diary_views.createDiary, name='create_diary'),
]
