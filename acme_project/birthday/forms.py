from django import forms

from . import models


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = models.Birthday

        fields = '__all__'

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
