from django import forms
from .models import PosDevice, PosAssignment, SimCard


class PosDeviceConfigForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()

    class Meta:
        model = PosDevice
        fields = ['description', 'imei', 'organization', 'is_trashed']

    def clean(self):
        super(PosDeviceConfigForm, self).clean()
        c_imei = self.cleaned_data.get('imei')
        imei_check = PosDevice.objects.filter(imei__icontains=c_imei)
        if imei_check:
            self.add_error('imei', 'Device  Already Exists')
        return self.cleaned_data


class PosAssignmentConfigForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()

    class Meta:
        model = PosAssignment
        fields = ['pos_device', 'sim_card', 'is_trashed']

    def clean(self):
        super(PosAssignmentConfigForm, self).clean()
        c_pos_device = self.cleaned_data.get('pos_device')
        pos_device_check = PosAssignment.objects.filter(pos_device__icontains=c_pos_device)
        pos_status_check = PosAssignment.objects.get(pos_device=c_pos_device)
        if pos_device_check and pos_status_check.is_trashed == False:
            self.add_error('pos_device', 'Device Not Available For Assignment')
        return self.cleaned_data


class SimCardConfigForm(forms.ModelForm):
    is_trashed = forms.CheckboxInput()

    class Meta:
        model = SimCard
        fields = ['sim_serial_number', 'sim_number', 'organization', 'is_active', 'is_trashed']

    def clean(self):
        # data from the form is fetched using super function
        super(SimCardConfigForm, self).clean()
        # extract the sim_serial_number and text field from the data
        c_sim_serial_number = self.cleaned_data.get('sim_serial_number')
        c_sim_number = self.cleaned_data.get('sim_number')
        sim_serial_number_check = SimCard.objects.filter(sim_serial_number__icontains=c_sim_serial_number)
        sim_number_check = SimCard.objects.get(sim_number_device=c_sim_number)
        # check whether  sim_serial_number already exists
        if sim_serial_number_check:
            self.add_error('sim_serial_number', 'Serial Number Already Exists')
        elif sim_number_check:
            self.add_error('c_sim_number', 'Serial Number Already Exists')
        return self.cleaned_data
