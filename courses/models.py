from django.db import models
from memberships.models import Membership
from django.contrib.auth.models import User
from django.urls import reverse

class Klasa(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length= 200, null=True)
    image = models.ImageField(upload_to='cat_images', default='cat_images/default.jpg')

    def __str__(self):
        return '{}'.format(self.title)

class Lendet(models.Model):
    creator = models.ForeignKey(User,on_delete = models.CASCADE)
    slug = models.SlugField()
    title = models.CharField(max_length=30)
    program = models.ForeignKey(Klasa,on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    created_on = models.DateTimeField(auto_now=True)
    course_image = models.ImageField(upload_to='kurs_images', default='default.jpg')
    course_books_link =models.CharField(max_length=100,default='null')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"slug": self.slug})

    def get_courses_related_to_memberships(self):
        return self.courses.all()

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')




class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=30)
    course = models.ForeignKey(Lendet,on_delete=models.CASCADE)
    video_id = models.CharField(max_length=11)
    position = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:lesson_detail", kwargs={"course_slug": self.course.slug,'lesson_slug':self.slug})
