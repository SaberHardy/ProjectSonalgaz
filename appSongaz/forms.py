from django import forms
from .models import File


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].widget = forms.ClearableFileInput(
            attrs={'class': 'custom-file-input',
                   'type': 'file'})
