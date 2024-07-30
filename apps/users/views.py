from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.contrib.auth import authenticate, login
from .models import UserProfile
from .serializers import UserProfileSerializer, CustomTokenObtainPairSerializer

class UserRegisterView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request, *args, **kwargs):
        phone_number = request.query_params.get('phone_number')
        if not phone_number:
            return Response({'detail': 'Phone number is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_profile = UserProfile.objects.get(phone_number=phone_number)
        except UserProfile.DoesNotExist:
            raise NotFound('UserProfile with this phone number does not exist.')

        serializer = self.get_serializer(user_profile)
        return Response(serializer.data)

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
