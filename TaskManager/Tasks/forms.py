from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = [
            'title',
            'description',
            'deadline',
            'completed',
            'category',
            'priority'   # ⭐ ADD THIS
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'glass-input',
                'placeholder': 'Enter task title'
            }),

            'description': forms.Textarea(attrs={
                'class': 'glass-input',
                'placeholder': 'Enter description',
                'rows': 3
            }),

            'deadline': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'glass-input'
            }),

            'completed': forms.CheckboxInput(attrs={
                'class': 'glass-checkbox'
            }),

            'category': forms.Select(attrs={
                'class': 'glass-input'
            }),

            # ⭐ NEW PRIORITY DROPDOWN
            'priority': forms.Select(attrs={
                'class': 'glass-input'
            }),
        }