from django.contrib import admin
from .models import (
    Subject,
    Teacher,
    SchoolClass,
    Student,
    Schedule,
    Grade,
)

admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(SchoolClass)
admin.site.register(Student)
admin.site.register(Schedule)
admin.site.register(Grade)