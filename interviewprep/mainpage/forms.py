from django import forms 
from .models import InitialInput

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = InitialInput
        fields = ('vieweeName', 'vieweeInfo', 'resume', 'position', 'context')
        