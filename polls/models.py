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
