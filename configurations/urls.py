from django.urls import path, include
from . import views

app_name = 'system_config'
urlpatterns = [

    path('country/', views.configure_country, name="country-config"),
    path('county/', views.county_config, name='conty-config'),
    path('subcounty/', views.sub_county_config, name='subcounty-config'),
    path('ward/', views.ward_config, name='ward-config'),
    path('zone/', views.zone_config, name='zone-config'),
    # revenue configs
    path('revenue/source/', views.revenue_source_config, name="r_source-config"),
    path('revenue/type/', views.revenue_type_config, name="r_type-config"),
    path('revenue/chart/of/account/', views.revenue_category_config, name="r_cat-config"),
    path('revenue/chart/of/account/', views.revenue_sub_category_config, name="r_sub-cat-config"),
    path('revenue/units/of/measure/', views.units_of_measure_config, name="r_units_of_measure-config"),
    path('revenue/payment/channel/', views.payment_channel_config, name="r_payment_channel_config"),
    path('revenue/financial/year/', views.financial_year_config, name="r_financial_year-config"),
    path('id/type/', views.id_type_config, name="r_id_type-config"),
    path('revenue/cost/matrix/', views.revenue_cost_matrix_config, name="r_cost-matrix"),
    # organizations config
    path('organization/', include('organizations.urls', namespace='org_config')),
]
