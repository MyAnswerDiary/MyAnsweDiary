from django.contrib import admin

from .models import Answer365, Diary, Question365

# Register your models here.

admin.site.register(Diary)

@admin.register(Question365)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['question', 'category', 'num']
    list_display_links = ['question', 'category', 'num']

@admin.register(Answer365)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer', 'question', 'created_at']
    list_display_links = ['answer', 'question', 'created_at']