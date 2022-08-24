from codecs import backslashreplace_errors
from datetime import datetime
from time import time
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['complete']

class Question(models.Model):
    ques = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True, blank=True)
    ques_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ques

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ques = models.ForeignKey(Question, related_name='question',on_delete=models.CASCADE, null=False, blank=False)
    ans_date = models.DateField(auto_now_add=True)
    ans_time = models.TimeField(auto_now_add=True)
    points = models.IntegerField()
    language = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.language

    

