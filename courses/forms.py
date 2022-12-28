from django import forms
from django.contrib.auth.models import User
from .models import Klasa, Lendet, Lesson



class KlasaForm(forms.ModelForm):
    class Meta:
        model = Klasa
        fields = '__all__'
        help_texts = {
            'title': 'The title name of the program goes here. It should have the level attached if necessary. For example: Computer Engineering 2',
            'description':'Enter a short description of the program',
            'image':'You can put a picture of the program or you can leave it blank'
        }

class LendaForm(forms.ModelForm):
    class Meta:
        model = Lendet
        fields = ['creator','slug', 'title', 'program', 'description', 'course_image','course_books_link']
        help_texts = {
            'title': 'The title name of the course under selected program goes here',
            'description':'Enter a short description of the program',
            'program':'Select the program for which you will create the course',
            'course_image':'You can put a picture of the course or you can leave it blank',
            'course_books_link' : 'Kindly put in a link to the cloud storage folder of the course books(e.g.:Google Drive)'
        }
        labels = {
            'title':'Title of the course'
        }
        widgets = {'creator': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class MesimiForm(forms.ModelForm):
    class Meta:
        model = Lesson 
        fields = ['slug','title', 'course', 'video_id', 'position', ]
        help_texts = {
            'title':'Enter the title of the lesson',
            'course':'Choose the course to which this lesson belongs',
            'video_id':'Enter the ID of the video from YouTube that you will upload (<a href="/krijo/mesim/youtube_help"> where can I find the ID</a>)',
            'position':'Enter the position number or teaching sequence'
        }
        widgets = {
            'slug': forms.HiddenInput()
        }