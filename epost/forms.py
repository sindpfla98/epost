from django import forms
from .models import CVSUpload

class CVSUploadForm(forms.ModelForm):
    class Meta:
        model = CVSUpload
        fields = ('file',)

    def __init__(self, *args, **kwargs):
        super(CVSUploadForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False