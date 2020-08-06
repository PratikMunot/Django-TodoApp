from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))
    class Meta:
        # we need to give minimum 2 values
        # first is for which model are we trying to ceate form for
        model = Task
        # what fields are we going to allow in that form
        fields='__all__'

# from form we import it in view and from view we import it in template
