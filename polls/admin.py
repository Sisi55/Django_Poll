from django.contrib import admin

from polls.models import Question, Choice


class ChoiceInline(admin.StackedInline):
    """
    답변 항목도 같이 등록하고 수정할 수 있게 추가한다.
    Choice 모델을 위한 옵션 클래스를 만드는데
    StackedInline 클래스를 상속받는다
    만든 클래스를 QustionAdmin 클래스의 inlines 클래스 변수에 추가한다
    """
    model = Choice
    extra = 3  # 화면에서 몇 개가 보이는지 ?


class QuestionAdmin(admin.ModelAdmin):
    """
    fieldsets 변수를 이용해 입력/수정 화면에서
    각 항목들을 그룹화 하고, 그룹의 이름을 설정한다
    (그룹이름, 그룹화항목들) ?
    """
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
