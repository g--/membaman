from django.contrib import admin

# Register your models here.
from fees.models import Year
from fees.models import SubYear
from fees.models import Income

class YearAdmin(admin.ModelAdmin):
        list_display = ['name', 'organisation', 'start', 'end']
        list_filter = ['organisation', 'start']

class SubYearAdmin(admin.ModelAdmin):
        list_display = ['year_name', 'organisation_name', 'name', 'start', 'end']
        list_filter = ['year__name', 'year__organisation']

admin.site.register(Year, YearAdmin)
admin.site.register(SubYear, SubYearAdmin)
admin.site.register(Income)
