"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rcs.settings import production

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='rcs-users')),
    path('users/api/v1/', include('users.api.urls', namespace='rcs-users-api')),
    # configuration urls
    path('config/', include('configurations.urls', namespace='system-config')),
    path('pos/', include('pos.urls', namespace='pos-devices')),
]

if production.DEBUG:
    urlpatterns += static(production.MEDIA_URL, document_root=production.MEDIA_ROOT)
