from django.contrib import admin
from .models import CityRecord, CountryRecord

# Register your models here.


admin.site.register(CountryRecord)
admin.site.register(CityRecord)
