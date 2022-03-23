from django import forms
from flow.models import Document, Person

# forms
class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['description', 'document']

class EditDocument(forms.ModelForm):
    class Meta:
        model = Person
        fields =[ 'first_name', 'last_name', 'email', 'gender', 'ip_address']