import django_filters
from django import forms
from .models import *

class CollectionFilter(django_filters.FilterSet):
    class Meta:
        model = Collection
        fields = ['title', 'desease_term']
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'widget': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
                },
            },
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'widget': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
                },
            },
        }