from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    teachers = models.ManyToManyField('Teacher', related_name='students')

    def __str__(self):
        return self.student_name

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)

    def __str__(self):
        return self.teacher_name


class Certificate(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    token = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"Certificate for {self.teacher} and {self.student}"
