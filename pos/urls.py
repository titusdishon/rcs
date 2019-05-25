from django.urls import path
from . import views

app_name = 'pos-devices'

urlpatterns = [
    path('pos/device/config/', views.pos_device_config, name='add_pos_device'),
    path('pos/assignment/config/', views.pos_assignment_config, name='assign_pos'),
    path('simcard/config/', views.simcard_config, name='add_simcard'),
]
