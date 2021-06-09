from polls.models import Task
from django.forms import ModelForm, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task', 'task2']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form_control',
                'placeholder': 'Введите ФИО'
            }),
            'task': TextInput(attrs={
                'class': 'form_control',
                'placeholder': 'Введите группу'}),
            'task2': TextInput(attrs={
                'class': 'form_control',
                'placeholder': 'Введите задолженность'}),
            }

