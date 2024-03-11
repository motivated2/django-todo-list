import datetime

from django import forms

from todo_list.models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }
        )
    )

    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "tags"
        ]
