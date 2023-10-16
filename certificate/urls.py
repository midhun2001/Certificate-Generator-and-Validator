from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list_view/', views.list_view, name='list_view'),
    path('teacher/<int:teacher_id>/', views.teacher, name='teacher'),
    path('student/<int:student_id>/', views.student, name='student'),
    path('generate_certificate/<int:teacher_id>/<int:student_id>', views.generate_certificate, name='generate_certificate'),
    path('verify_certificate/', views.verify_certificate, name='verify_certificate'),
]
