from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, create_user_profile

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-profile/', create_user_profile, name='create_user_profile'),
]
