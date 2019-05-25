from django.contrib import admin
from .models import Country, RevenueSource, RevenueType, ChartOfAccount, Ward

# Register your models here.
admin.site.register(Country)
admin.site.register(RevenueType)
admin.site.register(Ward)
admin.site.register(ChartOfAccount)


class RevenueSourceAdmin(admin.ModelAdmin):
    list_display = ['updated_on', 'created_on']


admin.site.register(RevenueSource, RevenueSourceAdmin)
