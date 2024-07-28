from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name', 'phone_number')
