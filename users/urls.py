from django.urls import path

from users.views import Profile, TutorRequest

app_name = 'users'

urlpatterns = [
    path('profile/', Profile, name='profile'),
    path('kerkesa/', TutorRequest, name='kerkesa')

]
