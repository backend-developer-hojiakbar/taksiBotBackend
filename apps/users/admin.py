from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile


class UserProfileAdmin(BaseUserAdmin):
    # Define the fields to be used in displaying the User model.
    list_display = ('phone_number', 'first_name', 'last_name', 'is_active', 'is_staff', 'balance')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('phone_number', 'first_name', 'last_name')

    # Remove the ordering by 'date_joined' if it's not a field in your model
    ordering = ('phone_number',)

    # Define the fields to be used in the user creation form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'phone_number', 'password1', 'password2', 'first_name', 'last_name', 'passport_photo', 'prava_photo',
            'balance'),
        }),
    )

    # Define the fields to be used in the user detail form
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'passport_photo', 'prava_photo', 'balance')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),  # You might have 'last_login', but not 'date_joined'
    )

    add_form_template = 'admin/auth/user/add_form.html'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form

admin.site.register(UserProfile, UserProfileAdmin)
