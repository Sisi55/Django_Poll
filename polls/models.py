import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(
        max_length=200
    )
    pub_date = models.DateTimeField(
        'date published'
    )

    def __str__(self):
        """
        관리자 화면이나 쉘에서 객체를 출력할 때 나타날 내용을 결정한다
        :return:
        """

        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date' # 정렬 기준
    # 원칙적으로 메서드에 의한 값은 정렬이 불가능함.
    # 대신 다른 값을 기준으로 정렬할 수 있다
    was_published_recently.boolean = True # 아이콘 모양
    # 값이 불리언 값 형태인지 설정한다. True이면 값 대신 아이콘 출력된다
    was_published_recently.short_description = 'Published recently?' # 인덱스 이름
    # 항목의 헤더 이름을 설정한다


class Choice(models.Model):
    question = models.ForeignKey(  # 포함되는 쪽에서 갖는다 ?
        Question,
        on_delete=models.CASCADE
    )
    choice_text = models.CharField(
        max_length=200
    )
    votes = models.IntegerField(
        default=10
    )

    def __str__(self):
        return self.choice_text
