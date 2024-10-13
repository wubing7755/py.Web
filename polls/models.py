import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

'''
包含问题描述和发布时间
'''
class Question(models.Model):
    # fields
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    # funcs
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
'''
包含选项描述和得票数
'''
class Choice(models.Model):
    # fields
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # funcs
    def __str__(self):
        return self.choice_text
    