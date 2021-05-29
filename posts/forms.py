from django import forms
from .models import Csv, Post


class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('File name',)

