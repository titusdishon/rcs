from django import forms
from .models import Organization, OrganizationCategory


class OrganizationCategoryConfigForm(forms.ModelForm):
    class Meta:
        model = OrganizationCategory
        fields = ['name']


class OrganizationConfigForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['code', 'name', 'category', 'organization_parent', 'county', 'sub_county', 'ward']
