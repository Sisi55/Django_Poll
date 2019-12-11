from django.contrib import admin

from polls.models import Question
# Register your models here.
# 만든 모델을 관리하려면 등록해야 한다
admin.site.register(Question)