from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User, UserType, RoleCenter, UserStatus, CountyAgent, Citizen


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        # fields = "__all__"
        exclude = ('user_permissions', 'groups', 'last_login', 'password',)
    def clean(self):

        # data from the form is fetched using super function
        super(UserRegisterForm, self).clean()
        # extract the username and text field from the data
        c_name = self.cleaned_data.get('username')
        name_check = User.objects.filter(username__iexact=c_name)
        # conditions to be met for the username length
        if name_check:
            self.add_error('username', 'Username Is Taken')
        return self.cleaned_data


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'phone']


class UserTypeConfigForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()

    class Meta:
        model = UserType
        fields = ['name', 'is_trashed']

    def clean(self):
        # data from the form is fetched using super function
        super(UserTypeConfigForm, self).clean()
        # extract the username and text field from the data
        c_name = self.cleaned_data.get('name')
        name_check = UserType.objects.filter(name__icontains=c_name)
        # conditions to be met for the username length
        if name_check:
            self.add_error('name', 'User Type Already Exists')
        return self.cleaned_data


class RoleCenterConfigForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()

    class Meta:
        model = RoleCenter
        fields = ['name', 'is_trashed']

    def clean(self):
        # data from the form is fetched using super function
        super(RoleCenterConfigForm, self).clean()
        # extract the username and text field from the data
        c_name = self.cleaned_data.get('name')
        name_check = RoleCenter.objects.filter(name__icontains=c_name)
        # conditions to be met for the username length
        if name_check:
            self.add_error('name', 'Role Type Already Exists')
        return self.cleaned_data


class CountyAgentonfigForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()

    class Meta:
        model = CountyAgent
        fields = ['name', 'registration_number', 'kra_pin_number', 'sub_county', 'ward', 'physical_address', 'email',
                  'mobile', 'postal_address', 'apply_flat_commission', 'commission', 'is_trashed']

    def clean(self):
        # data from the form is fetched using super function
        super(CountyAgentonfigForm, self).clean()
        # extract the username and text field from the data
        c_name = self.cleaned_data.get('name')
        registration_number = self.cleaned_data['registration_number']
        kra_pin_number = self.cleaned_data['kra_pin_number']
        name_check = CountyAgent.objects.filter(name__icontains=c_name)
        registration_number_check =  CountyAgent.objects.filter(registration_number__icontains=registration_number )
        kra_pin_number_check =  CountyAgent.objects.filter(kra_pin_number__icontains= kra_pin_number)

        # conditions to be met for the username length
        if name_check:
            self.add_error('name', 'Agent Already Exists')
        if registration_number_check:
            self.add_error('registration_number', 'Agent With That Registration Exists')
        if kra_pin_number_check:
            self.add_error('kra_pin_number', "Agent with that kra pin already exists")
        return self.cleaned_data


class CitizenCreationForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()

    class Meta:
        model = Citizen
        fields = ['name', 'id_type', 'id_number', 'kra_pin', 'nationality', 'is_county_resident', 'county',
                  'sub_county', 'ward', 'allow_system_access', 'create_wallet_account', 'is_trashed']

    def clean(self):
        # data from the form is fetched using super function
        super(CitizenCreationForm, self).clean()
        # extract the username and text field from the data
        c_name = self.cleaned_data.get('name')
        id_number = self.cleaned_data['registration_number']
        kra_pin_number = self.cleaned_data['kra_pin']
        name_check = Citizen.objects.filter(name__icontains=c_name)
        id_number_check = Citizen.objects.filter(id_number=id_number)
        kra_pin_check = Citizen.objects.filter(kra_pin__icontains=kra_pin_number)

        # conditions to be met for the username length
        if name_check:
            self.add_error('name', 'User Already Already Exists')
        if id_number_check:
            self.add_error('registration_number', 'Citizen With That Registration Exists')
        if kra_pin_check:
            self.add_error('kra_pin_number', "Citizen with that kra pin already exists")
        return self.cleaned_data

