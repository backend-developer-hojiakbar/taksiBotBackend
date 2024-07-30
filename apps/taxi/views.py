from rest_framework import viewsets, permissions, status
from .models import Request, GetRequest, BalansYechish, BalansToldirish
from .serializers import RequestSerializer, GetRequestSerializer, BalansYechishSerializer, BalansToldirishSerializer
from rest_framework import generics
from .permissions import IsActiveUser
from rest_framework.response import Response
from rest_framework import serializers
from apps.users.models import UserProfile
from django.db import transaction


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user_profile = self.request.user.userprofile  # Assuming `userprofile` is linked to your authentication system
        serializer.save(user=user_profile)


class GetRequestViewSet(viewsets.ModelViewSet):
    queryset = GetRequest.objects.all()
    serializer_class = GetRequestSerializer
    permission_classes = [IsActiveUser]

    def perform_create(self, serializer):
        user_profile = self.request.user.userprofile  # Assuming `userprofile` is linked to your authentication system
        serializer.save(user=user_profile)

    def get_queryset(self):
        queryset = super().get_queryset()
        request_id = self.request.query_params.get('request_id')
        if request_id:
            queryset = queryset.filter(request_id=request_id)
        return queryset


class ActiveRequestSearchView(generics.ListAPIView):
    serializer_class = RequestSerializer

    def get_queryset(self):
        queryset = Request.objects.filter(is_active=True)
        where = self.request.query_params.get('where', None)
        whereTo = self.request.query_params.get('whereTo', None)
        if where:
            queryset = queryset.filter(where=where)
        if whereTo:
            queryset = queryset.filter(whereTo=whereTo)
        return queryset


class BalansToldirishViewSet(viewsets.ModelViewSet):
    queryset = BalansToldirish.objects.all()
    serializer_class = BalansToldirishSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            summa = serializer.validated_data['summa']
            print("User avvalgi summa = ", user.balance)
            user.balance += summa
            print("QOshilgandan keyingi = ", user.balance)
            user.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BalansYechishViewSet(viewsets.ModelViewSet):
    queryset = BalansYechish.objects.all()
    serializer_class = BalansYechishSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            summa = serializer.validated_data['summa']
            if user.balance >= summa:
                user.balance -= summa
                user.save()
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Insufficient funds"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
