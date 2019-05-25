from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
# form imports
from .forms import (CountryConfigForm
, RevenueTypeConfigForm
, RevenueSourceConfigForm, UnitOfMeasureConfigForm
, ChartOfAccountConfigForm, FinancialYearConfigForm
, RevenueCategoryConfigForm, PaymentChannelConfigForm
, SubCountyConfigForm, IdTypeConfigForm
, WardConfigForm, RevenueSubCategoryConfigForm, RevenueCostMatrixForm
, ZoneConfigForm, CountyConfigForm)
from .models import Country, RevenueType, RevenueSource, Ward, SubCounty


# methods for configurtions
@login_required()
def configure_country(request):
    countries = Country.objects.all()
    for ct in countries:
        print(ct)
    if request.method == "POST":
        form = CountryConfigForm(request.POST)
        form.instance.created_by = request.user
        if form.is_valid():
            form.instance.code = form.cleaned_data['code'].upper()
            form.save()
            return redirect("system-config:country-config")
    else:
        form = CountryConfigForm()
    return render(request, 'configurations/locations/country_config.html',
                  {'form': form, 'countries':countries})


@login_required()
def county_config(request):
    if request.method == "POST":
        form = CountyConfigForm(request.POST)
        form.instance.created_by = request.user
        form.instance.created_on = timezone.now()
        if form.is_valid():
            form.save()
        return redirect('system-config:conty-config')
    else:
        form = CountyConfigForm()
    return render(request, 'configurations/locations/county_config.html',
                  {'form': form})


@login_required()
def sub_county_config(request):
    subcounties  = SubCounty.objects.all()
    for sbc in subcounties:
        print(sbc)
    if request.method == "POST":
        form = SubCountyConfigForm(request.POST)
        form.instance.created_by = request.user
        form.instance.created_on = timezone.now()
        if form.is_valid():
            form.save()
        return redirect('system-config:subcounty-config')
    else:
        form = SubCountyConfigForm()
    return render(request, 'configurations/locations/subcounty_config.html',
                  {'form': form})


@login_required()
def ward_config(request):
    if request.method == "POST":
        form = WardConfigForm(request.POST)
        form.instance.created_by = request.user
        form.instance.created_on = timezone.now()
        if form.is_valid():
            form.save()
        return redirect('system-config:ward-config')
    else:
        form = WardConfigForm()
    return render(request, 'configurations/locations/ward_config.html',
                  {'form': form})


@login_required()
def zone_config(request):
    if request.method == "POST":
        form = ZoneConfigForm(request.POST)
        form.instance.created_by = request.user
        form.instance.created_on = timezone.now()
        if form.is_valid():
            form.save()
        return redirect('system-config:zone-config')
    else:
        form = ZoneConfigForm()
    return render(request, 'configurations/locations/zone_config.html',
                  {'form': form})


# revenue configurations


@login_required()
def revenue_cost_matrix_config(request):
    # view_method = "Revenue Cost Matrix"
    all_r_types = RevenueType.objects.all()
    if request.method == "POST":
        form = RevenueCostMatrixForm(request.POST)
        form.instance.created_by = request.user
        form.instance.created_on = timezone.now()
        if form.is_valid():
            form.save()
        return redirect('system-config:r_type-config')
    else:
        form = RevenueCostMatrixForm()
    return render(request, 'configurations/revenue/revenue_configurations.html',
                  {'form': form, 'all_r_types': all_r_types})


@login_required()
def revenue_type_config(request):
    all_r_types = RevenueType.objects.all()
    if request.method == "POST":
        form = RevenueTypeConfigForm(request.POST)
        form.instance.created_by = request.user
        form.instance.created_on = timezone.now()
        if form.is_valid():
            form.save()
        return redirect('system-config:r_type-config')
    else:
        form = RevenueTypeConfigForm()
    return render(request, 'configurations/revenue/revenue_types_config.html',
                  {'form': form, 'all_r_types': all_r_types})


@login_required()
def revenue_source_config(request):
    all_r_sources = RevenueSource.objects.all()
    if request.method == "POST":
        form = RevenueSourceConfigForm(request.POST)
        form.instance.created_by = request.user
        form.instance.created_on = timezone.now()
        if form.is_valid():
            form.save()
        return redirect('system_config:r_source-config')
    else:
        form = RevenueSourceConfigForm()
    return render(request, 'configurations/revenue/revenue_configurations.html',
                  {'form': form, 'all_r_sources': all_r_sources})


@login_required
def chart_of_acount_config(request):
    if request.method == "POST":
        form = ChartOfAccountConfigForm(request.POST)
        form.instance.created_by = request.user
        form.instance.created_on = timezone.now()
        if form.is_valid():
            form.save()
        return redirect()
    else:
        form = ChartOfAccountConfigForm()
    return render(request, 'configurations/revenue/', {'form': form})


@login_required()
def revenue_category_config(request):
    if request.method == "POST":
        form = RevenueCategoryConfigForm(request.POST)
        form.instance.created_by = request.user
        form.instance.created_on = timezone.now()
        if form.is_valid():
            form.save()
        return redirect('system-config:r_cat-config')
    else:
        form = RevenueCategoryConfigForm()
    return render(request, 'configurations/revenue/revenue_category_config.html',
                  {'form': form})


@login_required()
def revenue_sub_category_config(request):
    if request.method == "POST":
        form = RevenueSubCategoryConfigForm(request.POST)
        form.instance.created_by = request.user
        form.instance.created_on = timezone.now()
        if form.is_valid():
            form.save()
        return redirect('system-config:r_sub-cat-config')
    else:
        form = RevenueSubCategoryConfigForm()
    return render(request, 'configurations/revenue/revenue_sub_cat_config.html',
                  {'form': form})


@login_required()
def units_of_measure_config(request):
    if request.method == "POST":
        form = UnitOfMeasureConfigForm(request.POST)
        form.instance.created_by = request.user
        form.instance.created_on = timezone.now()
        if form.is_valid():
            form.save()
        return redirect('system-config:r_sub-cat-config')
    else:
        form = UnitOfMeasureConfigForm()
    return render(request, 'configurations/revenue/revenue_sub_cat_config.html',
                  {'form': form})


@login_required()
def financial_year_config(request):
    if request.method == "POST":
        form = FinancialYearConfigForm(request.POST)
        form.instance.created_by = request.user
        form.instance.created_on = timezone.now()
        if form.is_valid():
            form.save()
        return redirect('system-config:r_sub-cat-config')
    else:
        form = FinancialYearConfigForm()
    return render(request, 'configurations/revenue/revenue_sub_cat_config.html',
                  {'form': form})


@login_required()
def payment_channel_config(request):
    if request.method == "POST":
        form = PaymentChannelConfigForm(request.POST)
        form.instance.created_by = request.user
        form.instance.created_on = timezone.now()
        if form.is_valid():
            form.save()
        return redirect('system-config:r_sub-cat-config')
    else:
        form = PaymentChannelConfigForm()
    return render(request, 'configurations/revenue/revenue_sub_cat_config.html',
                  {'form': form})


@login_required()
def id_type_config(request):
    if request.method == "POST":
        form = IdTypeConfigForm(request.POST)
        form.instance.created_by = request.user
        form.instance.created_on = timezone.now()
        if form.is_valid():
            form.save()
        return redirect('system-config:r_sub-cat-config')
    else:
        form = IdTypeConfigForm()
    return render(request, 'configurations/revenue/revenue_sub_cat_config.html',
                  {'form': form})
