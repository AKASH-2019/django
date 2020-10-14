from django import forms
from .models import Writer, Publication, Subject

class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = '__all__'

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'

