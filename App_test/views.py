from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse
from App_test.forms import MCQForm, WrittenForm, AnswerPaperForm
from App_test.models import Written
from App_test.models import MCQ
import time


# Create your views here.
def mutiple_choice_quiz(request):
    mcq = MCQ.objects.all()
    return render(request, "App_test/mcqTest.html", context={'exam': mcq})


@login_required
def written_exam_sys(request):
    theQuestion = Written.objects.all()
    QuestionForm = WrittenForm()
    if request.method == 'POST':
        form = WrittenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Home'))
    return render(request, "App_test/writtenTest.html",
                  context={'QuestionForm': QuestionForm, 'Question': theQuestion})


def written_exam_answer_paper(request, sub, exam_type):
    theQuestion = Written.objects.all().filter(Subject=sub).filter(Exam_title=exam_type)
    # print(theQuestion)
    questionList = list(theQuestion)[0]
    questionPaper = questionList.Question_file
    t = int(questionList.Duration)
    t = t * 3600
    AnswerForm = AnswerPaperForm()
    if request.method == 'POST':
        AnswerForm = AnswerPaperForm(request.POST, request.FILES)
        if AnswerForm.is_valid():
            form = AnswerForm.save(commit=False)
            form.answerer = request.user
            form.exam_type = str(exam_type) + " " + str(sub)
            form.save()
            return HttpResponseRedirect(reverse('Home'))
    return render(request, "App_test/Answer_sheet.html",
                  context={'answerform': AnswerForm, 'QuestionPaper': questionPaper, 'Duration': t, 'subject': sub,
                           'exam_type': exam_type})
