from django.db import models
from App_Attendance.models import Course

# Create your models here.
from App_login.models import StudentInfo


class MCQ(models.Model):
    question = models.CharField(max_length=254)
    option1 = models.CharField(max_length=254)
    option2 = models.CharField(max_length=254)
    option3 = models.CharField(max_length=254)
    option4 = models.CharField(max_length=254)
    correct_answer = models.CharField(max_length=254)


class Written(models.Model):
    Subject = models.CharField(max_length=256)
    Duration = models.CharField(max_length=2)
    Exam_title = models.CharField(max_length=120)
    Question_file = models.FileField(upload_to='written_question')
    Publish_Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Exam_title} + {self.Subject}"


class WrittenExamAnswerPaper(models.Model):
    answerer = models.ForeignKey(StudentInfo, on_delete=models.CASCADE, related_name='answerer')
    exam_type = models.ForeignKey(Written, on_delete=models.CASCADE, related_name='exam_type')
    Answer_paper = models.FileField(upload_to='answer_paper')
    Submit_time = models.TimeField(auto_created=True)
