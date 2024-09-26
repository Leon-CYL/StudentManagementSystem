from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentId', 'first_name', 'last_name', 'email', 'major', 'gpa']
        labels = {
            'studentId': 'Student ID',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'major': 'Major',
            'gpa': 'GPA'
        }
        widgets = {
            'studentId': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'major': forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'})
        }
