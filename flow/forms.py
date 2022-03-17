from django import forms
from flow.models import Document

# forms
class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['description', 'document']