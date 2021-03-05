from django.contrib.auth.forms import forms
from App_test.models import MCQ, Written, WrittenExamAnswerPaper


class MCQForm(forms.ModelForm):
    class Meta:
        model = MCQ
        fields = "__all__"


class WrittenForm(forms.ModelForm):
    class Meta:
        model = Written
        fields = ['Subject', 'Duration', 'Exam_title', 'Question_file']


class AnswerPaperForm(forms.ModelForm):
    class Meta:
        model = WrittenExamAnswerPaper
        fields = ['Answer_paper']
