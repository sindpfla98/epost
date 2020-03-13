from django import forms
from .models import CVSUpload, CallingPlan

class CVSUploadForm(forms.ModelForm):
    class Meta:
        model = CVSUpload
        fields = ('file',)

    def __init__(self, *args, **kwargs):
        super(CVSUploadForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False
        
class ListingForm(forms.ModelForm):
    class Meta:
        model = CallingPlan
        fields = ('mobile_carrier', 'category', 'data_speed')