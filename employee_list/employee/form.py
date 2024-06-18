from django import forms
from .models import EmployeeDetails

class EmpForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetails
        fields = '__all__'
        # fields = ['fullname', 'emp_no', 'phone', 'position']

        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'emp_no': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super(EmpForm, self).__init__(*args, **kwargs)
            self.fields['position'].empty_label = "Select Position"