from django.contrib import admin
from django.urls import path, include
from main.views import homeFeedView, testView, leaderboardView
from pages.views import aboutPageView, searchView
from questions.views import (questionView, newView, answerView,
                            myQuestionsView, myAnswersView, questionVoteView,
                            answerVoteView, questionReportView, questionReportConfirmView, 
                            answerReportView, answerReportConfrimView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeFeedView),
    path('test/', testView),
    path('leaderboard/', leaderboardView),
    path('search/', searchView, name='search'),
    path('about/', aboutPageView),
    path('accounts/', include('allauth.urls')),
    path('question/<int:id>/', questionView),
    path('question/<int:id>/vote', questionVoteView),
    path('answer/<int:id>/vote', answerVoteView),
    path('question/<int:id>/answer', answerView),
    path('question/new/', newView),
    path('question/my_answers/', myAnswersView, name='my-answers'),
    path('question/my_questions/', myQuestionsView, name='my-questions'),
    path('question/<int:id>/report/', questionReportView, name='question-report'),
    path('question/<int:id>/report/confirm/', questionReportConfirmView, name='question-report-confrim'),
    path('answer/<int:id>/report/', answerReportView, name='answer-report'),
    path('answer/<int:id>/report/confirm/', answerReportConfrimView, name='answer-report-confrim'),
]
