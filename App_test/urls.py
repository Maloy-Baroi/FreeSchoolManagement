from django.urls import path
from App_test import views

app_name = 'App_test'

urlpatterns = [
    path('mcq', views.mutiple_choice_quiz, name='mcq'),
    path('written', views.written_exam_sys, name='written_sys'),
    path('answer_paper/<sub>/<exam_type>', views.written_exam_answer_paper, name='answer_paper')
]
