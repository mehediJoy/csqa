from django.contrib import admin
from .models import Question, Answer

class CustomAnswer(admin.ModelAdmin):
    list_display = ('text', 'reported')
    list_filter = ('reported',)
class CustomQuestion(admin.ModelAdmin):
    list_display = ('title', 'reported')
    list_filter = ('reported',)

admin.site.register(Question, CustomQuestion)
admin.site.register(Answer, CustomAnswer)