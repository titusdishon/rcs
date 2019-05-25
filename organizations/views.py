from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import OrganizationCategoryConfigForm, OrganizationConfigForm
# Create your views here.


def organization_config(request):
    if request.method == 'POST':
        form = OrganizationConfigForm(request.POST)
        form.instance.created_by = request.user
        form.instance.created_on = timezone.now()
        if form.is_valid():
            form.save()
        return redirect('system-config:org_config:org-config')
    else:
        form = OrganizationConfigForm()
    return render(request, 'configurations/org_config.html', {'form': form})


def organization_category_config(request):
    if request.method == 'POST':
        form = OrganizationCategoryConfigForm(request.POST)
        form.instance.created_by = request.user
        form.instance.created_on = timezone.now()
        if form.is_valid():
            form.save()
        return redirect('system-config:org_config:org-cat-config')
    else:
        form = OrganizationCategoryConfigForm()
    return render(request, 'configurations/org_cat_config.html', {'form': form})
