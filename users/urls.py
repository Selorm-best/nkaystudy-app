from django.urls import path

from users.views import Profile, TutorRegister

app_name = 'users'

urlpatterns = [
    path('profile/', Profile, name='profile'),
    path('kerkesa/', TutorRegister, name='kerkesa')

]
