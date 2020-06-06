from django.forms import ModelForm
from .models import todoslist

class TodoCreationForm(ModelForm):
     class Meta:
       model = todoslist
       fields = ['title', 'memo', 'important']
