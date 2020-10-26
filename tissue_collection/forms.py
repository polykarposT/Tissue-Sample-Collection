from django import forms
from .models import Collection, Sample

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ('title', 'desease_term')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title', 'required': 'true', 'type': 'text'}),
            'desease_term': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Desease term', 'required': 'true', 'type': 'text'}),
        }

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ('donor_count','material_type')
        widgets = {
            'donor_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '90152', 'required': 'true', 'type': 'number', 'min':'0'}),
            'material_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '"Cerebrospinal fluid"', 'required': 'true', 'type': 'text'})
        }


class SampleUpdateForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ('collection','donor_count', 'material_type')
        widgets = {
            'collection': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select collection', 'required': 'true'}),
            'donor_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '90152', 'required': 'true', 'type': 'number', 'min': '0'}),
            'material_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '"Cerebrospinal fluid"', 'required': 'true', 'type': 'text'})
        }
