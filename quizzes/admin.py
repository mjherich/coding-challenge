from django.contrib import admin

from .models import Teacher, Student, Quiz, Question, Scorecard, Student_Answer

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Scorecard)
admin.site.register(Student_Answer)