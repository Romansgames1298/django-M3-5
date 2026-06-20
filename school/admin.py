from django.contrib import admin
from .models import Subject, Teacher, SchoolClass, Student


admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(SchoolClass)
admin.site.register(Student)