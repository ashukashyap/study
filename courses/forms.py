from django import forms
from django.contrib.auth.models import User
from .models import Klasa, Lendet, Lesson



class KlasaForm(forms.ModelForm):
    class Meta:
        model = Klasa
        fields = '__all__'
        help_texts = {
            'titulli': 'Add Title',
            'pershkrimi':'Write The Course Decripection',
            'imazhi':'Add Course Image'
        }

class LendaForm(forms.ModelForm):
    class Meta:
        model = Lendet
        fields = ['krijues','slug', 'titulli', 'klasa', 'pershkrimi', ]
        help_texts = {
            'titulli': 'Subject Title',
            'pershkrimi':'Write the Subject Description',
            'klasa':'Write the Category',
            
        }
        labels = {
            'titulli':'Title'
        }
        widgets = {'krijues': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class MesimiForm(forms.ModelForm):
    class Meta:
        model = Lesson 
        fields = ['slug','titulli', 'lenda', 'video_id', 'pozicioni', ]
        help_texts = {
            'titulli':'Title',
            'lenda':'Select The Course',
            'video_id':'Uplode the Youtube Video Id ',
            'pozicioni':'Write the Decripection '
        }
        widgets = {
            'slug': forms.HiddenInput()
        }