from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from .models import CityRecord, CountryRecord
from .serializers import CityRecordSerializer, CountryRecordSerializer


class CityRecordList(APIView):
    def get(self, request):
        serializer = CityRecordSerializer(CityRecord.objects.all(), many=True)
        return Response(serializer.data)


class CityRecordDetails(APIView):
    serializer_class = CityRecordSerializer

    def _get_object(self, city_name):
        return CityRecord.objects.get(pk=city_name)

    def get(self, request, city_name=None):
        try:
            city = self._get_object(city_name)
            serializer = CityRecordSerializer(city)
            return Response(serializer.data)
        except CityRecord.DoesNotExist as e:
            return Response(
                {'error': str(e)},
                status=HTTP_404_NOT_FOUND,
            )

    def post(self, request):
        serializer = CityRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, city_name):
        try:
            city = self._get_object(city_name)
        except CityRecord.DoesNotExist as e:
            return Response(
                {'error': str(e)},
                status=HTTP_404_NOT_FOUND
            )
        serializer = CityRecordSerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, city_name):
        city = CityRecord.objects.filter(name=city_name)[0]
        city.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class CountryRecordList(APIView):
    def get(self, request):
        serializer = CountryRecordSerializer(CountryRecord.objects.all(), many=True)
        return Response(serializer.data)


class CountryRecordDetails(APIView):
    serializer_class = CountryRecordSerializer

    def _get_object(self, country_name):
        return CountryRecord.objects.get(pk=country_name)

    def get(self, request, country_name=None):
        try:
            country = self._get_object(country_name)
            serializer = CountryRecordSerializer(country)
            return Response(serializer.data)
        except CountryRecord.DoesNotExist as e:
            return Response(
                {'error': str(e)},
                status=HTTP_404_NOT_FOUND,
            )

    def put(self, request, country_name):
        try:
            country = self._get_object(country_name)
        except CountryRecord.DoesNotExist as e:
            return Response(
                {'error': str(e)},
                status=HTTP_404_NOT_FOUND,
            )
        serializer = CountryRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, country_name):
        country = self._get_object(country_name)
        country.delete()
        return Response(request.data, status=HTTP_204_NO_CONTENT)

    def post(self, request):
        serializer = CountryRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)