from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from .forms import PosDeviceConfigForm, PosAssignmentConfigForm, SimCardConfigForm
# Create your views here.


@login_required()
def pos_device_config(request):
    if request.method == 'POST':
        form = PosDeviceConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pos-devices:add_pos_device')
        else:
            redirect('rcs-users:error_page')
    else:
        form = PosDeviceConfigForm()
    return render(request, 'pos/pos-device-config.html', {'form': form})


@login_required()
def pos_assignment_config(request):
    if request.method == 'POST':
        form = PosAssignmentConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pos-devices:assign_pos')
        else:
            redirect('rcs-users:error_page')
    else:
        form = PosAssignmentConfigForm()
    return render(request, 'pos/pos-assignment-config.html', {'form': form})


@login_required()
def simcard_config(request):
    if request.method == 'POST':
        form = SimCardConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pos-devices:add_simcard')
        else:
            redirect('rcs-users:error_page')
    else:
        form = SimCardConfigForm()
    return render(request, 'pos/sim-card-config.html', {'form': form})
