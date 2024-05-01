from django import forms

from .models import Employee


class EmployeeForm(forms.ModelForm):
    pan_card_pic_blob = forms.ImageField(required=False)

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'cv_file', 'photo_file']