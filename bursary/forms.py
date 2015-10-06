from django import forms
from bursary.models import Applicant

class BursaryForm(forms.ModelForm):
    class Meta:
        model = Applicant 
        fields = ('first_name', 'last_name', 'email', 'institution', 'supervisor')
 

    

