from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        profile = self.get_object()
        profile.is_active = True
        profile.save()
        return Response({'status': 'profile activated'}, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
def create_user_profile(request):
    if request.method == 'POST':
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

