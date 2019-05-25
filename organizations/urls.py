from django.urls import path

from . import views

app_name = 'org_config'
urlpatterns = [
    path('config/', views.organization_config, name="org-config"),
    path('category/config/', views.organization_category_config, name="org-cat-config"),
]
