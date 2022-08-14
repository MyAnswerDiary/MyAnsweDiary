from django.contrib import admin

from .models import Diary, Question365

# Register your models here.

admin.site.register(Diary)

@admin.register(Question365)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['question', 'category', 'num']
    list_display_links = ['question', 'category', 'num']