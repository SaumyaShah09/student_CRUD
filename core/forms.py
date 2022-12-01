from django import forms
from .models import Student
from django.forms import widgets

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name","roll","city")
        widgets = {
            'name':forms.TextInput(attrs={'class':'from-control'}),
            'roll':forms.NumberInput(attrs={'class':'from-control'}),
            'city':forms.TextInput(attrs={'class':'from-control'})
        }