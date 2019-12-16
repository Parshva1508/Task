from django import forms
from todolist.models import Tasklist
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasklist
        fields = ['task','done']

