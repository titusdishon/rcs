from django import forms
from users.models import IdType
from .models import (Country
, RevenueType
, RevenueSource
, ChartOfAccount
, RevenueCategory
, RevenueSubcategory, RevenueCostMatrix
, Ward, Zone, SubCounty, County
, FinancialYear, UnitOfMeasure, PaymentChannel)


# define the class of a form

class CountryConfigForm(forms.ModelForm):
    name = forms.CharField()
    is_trashed =forms.CheckboxInput()

    class Meta:
        model = Country
        fields = ['code', 'name','is_trashed']

    def clean(self):

        # data from the form is fetched using super function
        super(CountryConfigForm, self).clean()
        # extract the username and text field from the data
        c_code = self.cleaned_data.get('code')
        c_name = self.cleaned_data.get('name')
        name_check = Country.objects.filter(name__icontains=c_name)
        code_check = Country.objects.filter(code__icontains=c_code)
        # conditions to be met for the username length
        if code_check:
            self.add_error('code', 'Country With That Code Exists')
        if name_check:
            self.add_error('name', 'Country Already Exists')
        return self.cleaned_data


class CountyConfigForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()
    class Meta:
        model = County
        fields = ['code', 'name','is_trashed']

    def __init__(self, *args, **kwargs):
        super(CountyConfigForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True

    def clean(self):

        # data from the form is fetched using super function
        super(CountyConfigForm, self).clean()
        # extract the username and text field from the data
        c_code = self.cleaned_data.get('code')
        c_name = self.cleaned_data.get('name')
        name_check = County.objects.filter(name__icontains=c_name)
        code_check = County.objects.filter(code__icontains=c_code)
        # conditions to be met for the username length
        if code_check:
            self.add_error('code', 'County With That Code Exists')
        if name_check:
            self.add_error('name', '%(c_name)s Already Exists')
        return self.cleaned_data


class SubCountyConfigForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()
    class Meta:
        model = SubCounty
        fields = ['name', 'county','is_trashed']

    def __init__(self, *args, **kwargs):
        super(SubCountyConfigForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True

    def clean(self):

        # data from the form is fetched using super function
        super(SubCountyConfigForm, self).clean()
        # extract the username and text field from the data
        c_name = self.cleaned_data.get('name')
        name_check = SubCounty.objects.filter(name__icontains=c_name)
        # conditions to be met for the username length
        if name_check:
            self.add_error('name', '%(c_name)s Already Exists')
        return self.cleaned_data


class WardConfigForm(forms.ModelForm):
    name = forms.CharField()
    is_trashed = forms.CheckboxInput()

    class Meta:
        model = Ward
        fields = ['name', 'sub_county','is_trashed']

    def __init__(self, *args, **kwargs):
        super(WardConfigForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True

    def clean(self):

        # data from the form is fetched using super function
        super(WardConfigForm, self).clean()
        # extract the username and text field from the data
        c_name = self.cleaned_data.get('name')
        name_check = Ward.objects.filter(name__icontains=c_name)
        # conditions to be met for the username length
        if name_check:
            self.add_error('name', '%(c_name)s Already Exists')
        return self.cleaned_data


class ZoneConfigForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()
    class Meta:
        model = Zone
        fields = ['name', 'is_trashed']

    def __init__(self, *args, **kwargs):
        super(ZoneConfigForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True

    def clean(self):

        # data from the form is fetched using super function
        super(ZoneConfigForm, self).clean()
        # extract the username and text field from the data
        c_name = self.cleaned_data.get('name')
        name_check = Zone.objects.filter(name__icontains=c_name)
        # conditions to be met for the username length
        if name_check:
            self.add_error('name', '%(c_name)s Already Exists')
        return self.cleaned_data


# revenue config forms

class RevenueCostMatrixForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()

    class Meta:
        model = RevenueCostMatrix
        fields = ['financial_year', 'revenue_source', 'revenue_type', 'revenue_category', 'revenue_subcategory', 'cost', 'is_trashed']

    def __init__(self, *args, **kwargs):
        super(RevenueCostMatrixForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True


class RevenueTypeConfigForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()
    class Meta:
        model = RevenueType
        fields = ['revenue_source', 'name', 'pos_enabled', 'is_trashed']

    def __init__(self, *args, **kwargs):
        super(RevenueTypeConfigForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True


class RevenueSourceConfigForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()

    class Meta:
        model = RevenueSource
        fields = ['name', 'pos_enabled', 'general_ledger', 'is_trashed']

    def __init__(self, *args, **kwargs):
        super(RevenueSourceConfigForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True


class ChartOfAccountConfigForm(forms.ModelForm):
    class Meta:
        model = ChartOfAccount
        fields = ['gl_code', 'gl_name', 'is_trashed']

    def __init__(self, *args, **kwargs):
        super(ChartOfAccountConfigForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True


class RevenueCategoryConfigForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()

    class Meta:
        model = RevenueCategory
        fields = ['name', 'revenue_type', 'pos_enabled', 'is_trashed']

    def __init__(self, *args, **kwargs):
        super(RevenueCategoryConfigForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True


class RevenueSubCategoryConfigForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()

    class Meta:
        model = RevenueSubcategory
        fields = ['revenue_category', 'name', 'pos_enabled', 'is_trashed']

    def __init__(self, *args, **kwargs):
        super(RevenueSubCategoryConfigForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True


class FinancialYearConfigForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()

    class Meta:
        model = FinancialYear
        fields = ['name', 'start_on', 'end_on', 'is_trashed']

    def __init__(self, *args, **kwargs):
        super(FinancialYearConfigForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True


class UnitOfMeasureConfigForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()

    class Meta:
        model = UnitOfMeasure
        fields = ['name', 'revenue_type', 'is_trashed']

    def __init__(self, *args, **kwargs):
        super(UnitOfMeasureConfigForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True


class PaymentChannelConfigForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()

    class Meta:
        model = PaymentChannel
        fields = ['name', 'is_trashed']

    def __init__(self, *args, **kwargs):
        super(PaymentChannelConfigForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True


class IdTypeConfigForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()

    class Meta:
        model = IdType
        fields = ['name', 'is_trashed']

    def __init__(self, *args, **kwargs):
        super(IdTypeConfigForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True
