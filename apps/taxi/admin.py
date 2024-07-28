from django.contrib import admin
from .models import Request, GetRequest, BalansYechish, BalansToldirish


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'request_type', 'where', 'whereTo', 'yolovchiSoni', 'phone_number', 'is_active')
    search_fields = ('user__username', 'where', 'whereTo', 'yolovchiSoni', 'phone_number')


@admin.register(GetRequest)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'request', 'getrequest_type', 'where', 'whereTo')
    search_fields = ('request', 'where', 'whereTo')


@admin.register(BalansYechish)
class BalansYechish(admin.ModelAdmin):
    list_display = ('id', 'user', 'summa')


@admin.register(BalansToldirish)
class BalansToldirish(admin.ModelAdmin):
    list_display = ('id', 'user', 'summa')
