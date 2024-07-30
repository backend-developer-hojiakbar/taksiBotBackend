from rest_framework import serializers
from .models import Request, GetRequest, BalansToldirish, BalansYechish


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'user', 'request_type', 'where', 'whereTo', 'phone_number', 'is_active']
        read_only_fields = ('user',)


class GetRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = GetRequest
        fields = ['id', 'request', 'getrequest_type']
        read_only_fields = ('user',)


class BalansToldirishSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalansToldirish
        fields = ['id', 'user', 'summa']


class BalansYechishSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalansYechish
        fields = ['id', 'user', 'summa']