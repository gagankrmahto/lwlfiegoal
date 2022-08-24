from django.contrib import admin
from . models import Task,Question,Answer
# Register your models here.
from . models import *
class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines=[AnswerAdmin]
   
admin.site.register(Task)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)