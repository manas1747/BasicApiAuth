from rest_framework import serializers
from .models import CountryRecord, CityRecord


class CountryRecordSerializer(serializers.ModelSerializer):
    cities = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = CountryRecord
        fields = ('name', 'cities')


class CityRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityRecord
        fields = ('name', 'pincode', 'country')

    def create(self, validated_data):
        country = CountryRecord.objects.filter(
            name=validated_data['country']
        )[0]

        if not country:
            country = CountryRecord.objects.create(
                name=validated_data['country']
            )

        return CityRecord.objects.create(
            name=validated_data['name'],
            pincode=validated_data['pincode'],
            country=country
        )

    def update(self, instance, validated_data):
        country = CountryRecord.objects.filter(
            name=validated_data['country']
        )[0]

        instance.name = validated_data['name']
        instance.pincode = validated_data['pincode']
        instance.country = country
        instance.save()
        return instance
