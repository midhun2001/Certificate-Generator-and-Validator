from django.contrib import admin
from .models import Student, Teacher, Certificate

admin.site.register(Student)
admin.site.register(Teacher)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display=['teacher','student','token']