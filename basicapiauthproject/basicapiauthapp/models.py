from django.db import models

# Create your models here.


class CountryRecord(models.Model):
    name = models.CharField(max_length=100, default=None, primary_key=True)

    def __str__(self):
        return self.name


class CityRecord(models.Model):
    name = models.CharField(max_length=100, default=None, primary_key=True)
    pincode = models.CharField(max_length=10, default=None)
    country = models.ForeignKey(CountryRecord, on_delete=models.CASCADE, related_name="cities")

    def __str__(self):
        return self.name