from django.contrib import admin
#from courses.models import Courses,Lesson,Program
# Register your models here.
from courses.models import Lendet,Lesson,klasa
admin.site.register(Lendet)
admin.site.register(Lesson)
admin.site.register(klasa)
