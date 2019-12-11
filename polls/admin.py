from django.contrib import admin

from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    """

    """
    model = Choice
    extra = 3  # 화면에서 몇 개가 보이는지 ?


class QuestionAdmin(admin.ModelAdmin):
    """
    목록에 보이는 항목을 변경하려면
    list_display 클래스 변수를 추가합니다
    변수의 값은 튜플로 출력하고 싶은 항목을 묶어서 설정합니다
    """
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    list_display = ('question_text','pub_date','was_published_recently')
    # 클래스 변수/함수 가능 ?

    inlines = [ChoiceInline]
    
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
