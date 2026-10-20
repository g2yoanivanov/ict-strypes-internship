from rest_framework import serializers


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_lenght=64)
    age = serializers.IntegerField()
    city = serializers.CharField(max_lenght=64)