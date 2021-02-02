from django.urls import path, include
from .views import CityRecordList, CityRecordDetails, CountryRecordList, CountryRecordDetails


app_name = "basicapiauthapp"


urlpatterns = [
    path('cityrecords/list/', CityRecordList.as_view()),
    path('cityrecords/', CityRecordDetails.as_view()),
    path('cityrecords/<city_name>/', CityRecordDetails.as_view()),

    path('countryrecords/list/', CountryRecordList.as_view()),
    path('countryrecords/', CountryRecordDetails.as_view()),
    path('countryrecords/<country_name>/', CountryRecordDetails.as_view()),
]
