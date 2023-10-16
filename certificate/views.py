import jwt
from jwt.exceptions import DecodeError

from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Student, Teacher, Certificate
from .forms import TokenForm


def home(request):
    return render(request, 'home.html')

def list_view(request):
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    return render(request, 'list_view.html', {'teachers': teachers, 'students': students})

def teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    students = teacher.students.all()
    return render(request, 'teacher.html', {'teacher': teacher, 'students': students})

def student(request, student_id):
    student = Student.objects.get(id=student_id)
    teachers = student.teachers.all()
    return render(request, 'student.html', {'student': student, 'teachers': teachers})

def generate_certificate(request, teacher_id, student_id):
    certificate = Certificate.objects.filter(teacher_id=teacher_id, student_id=student_id).first()
    print(certificate)
    if not certificate:
        new_certificate = Certificate.objects.create(teacher_id=teacher_id, student_id=student_id)
        payload = {
                'certificate_id': new_certificate.id,
                'teacher_id': new_certificate.teacher_id,
                'student_id': new_certificate.student_id,
            }
        
        secret_key = 'course'
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        
        new_certificate.token = token
        new_certificate.save()

        return render(request, 'view_certificate.html', {'certificate': new_certificate})
    else:
        return render(request, 'view_certificate.html', {'certificate': certificate})


def verify_certificate(request):
    if request.method == 'POST':
        form = TokenForm(request.POST)
        if form.is_valid():

            token = form.cleaned_data['token']
            secret_key = 'course'
            try:
                payload = jwt.decode(token, secret_key, algorithms=['HS256'])

                certificate_id = payload.get('certificate_id')
                teacher_id = payload.get('teacher_id')
                student_id = payload.get('student_id')

                certificate = Certificate.objects.get(id=certificate_id)
                if (
                    certificate.teacher.id == teacher_id and
                    certificate.student.id == student_id
                ):
                    messages.success(request, "Certificate Is Valid")
                    return render(request, 'view_certificate.html', {'certificate': certificate})
                else:
                    messages.success(request, "Certificate Is Invalid")
                    return redirect('verify_certificate')
            except DecodeError:
                messages.success(request, "Certificate Is Invalid")
                return redirect('verify_certificate')
        
    else:
        form = TokenForm()
    return render(request, 'verify_certificate.html', {'form': form})
  