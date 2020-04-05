from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


# When Signing up users can opt to be a teacher or student
class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    userid = models.OneToOneField(User, on_delete=models.CASCADE)


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)


# A Quiz has a Teacher who wrote the quiz
class Quiz(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    teacherid = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()


# Answer integer choices (used in Question and Student_Answer)
class Answers(models.IntegerChoices):
    A = 0
    B = 1
    C = 2
    D = 3


# Questions are part of a quiz
class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    quizid = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    statement = models.TextField()

    # Multiple Choice answers
    choice0 = models.CharField(max_length=500)
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)

    answer = models.IntegerField(choices=Answers.choices)


# Scorecards are associated with a quiz and student
class Scorecard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    quizid = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)


# Student Answers are associated with a question and scorecard
class Student_Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    questionid = models.ForeignKey(Question, on_delete=models.CASCADE)
    scorecardid = models.ForeignKey(Scorecard, on_delete=models.CASCADE)
    answer = models.IntegerField(choices=Answers.choices)
    iscorrect = models.BooleanField()