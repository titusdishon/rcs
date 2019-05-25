from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm, UserTypeConfigForm, CitizenCreationForm, \
    CountyAgentonfigForm
from .models import User


class Home(LoginRequiredMixin, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/users.html'


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    context_object_name = 'form'
    fields = ['username', 'email', 'name', 'mobile', 'user_type', 'organization', 'role_center', 'agent', 'citizen',
              'user_status']
    template_name = 'users/update_user.html'
    success_url = reverse_lazy("rcs-users:home")


@login_required()
def error_page(request):
    return render(request, 'app/page_500.html')


@login_required()
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            return redirect('rcs-users:user_list')
        else:
            redirect('rcs-users:error_page')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('rcs-users:product_list')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'users/profile.html', context)


@login_required
def user_type(request):
    if request.method == "POST":
        u_type_form = UserTypeConfigForm(request.POST)
        if u_type_form.is_valid():
            u_type_form.save()
            return redirect('rcs-users:add_user_type')
    else:
        u_type_form = UserTypeConfigForm()
    context = {'u_type_form': u_type_form}
    return render(request, 'users/user-type.html', context)


@login_required
def role_center(request):
    if request.method == "POST":
        u_type_form = UserTypeConfigForm(request.POST)
        if u_type_form.is_valid():
            u_type_form.save()
            return redirect('rcs-users:add_user_role')
    else:
        u_type_form = UserTypeConfigForm()
    context = {'u_type_form': u_type_form}
    return render(request, 'users/role_center.html', context)


@login_required
def citizen_config(request):
    if request.method == "POST":
        u_type_form = CitizenCreationForm(request.POST)
        if u_type_form.is_valid():
            u_type_form.save()
            return redirect('rcs-users:add_user_role')
    else:
        u_type_form = CitizenCreationForm()
    context = {'u_type_form': u_type_form}
    return render(request, 'users/citizen_config.html', context)


@login_required
def agent_config(request):
    if request.method == "POST":
        u_type_form = CountyAgentonfigForm(request.POST)
        if u_type_form.is_valid():
            u_type_form.save()
            return redirect('rcs-users:add_user_role')
    else:
        u_type_form = CountyAgentonfigForm()
    context = {'u_type_form': u_type_form}
    return render(request, 'users/county_agent_config.html', context)
