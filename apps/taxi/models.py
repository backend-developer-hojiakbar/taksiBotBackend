from django.db import models
from apps.users.models import UserProfile
from core.models import BaseModel


class Request(BaseModel):
    user = models.ForeignKey(UserProfile, models.CASCADE)
    REQUEST_TYPE_CHOICES = [
        ('yolovchi_berish', 'Yolovchi berish'),
        ('pochta_berish', 'Pochta berish'),
    ]
    WHERE_TYPE_CHOICES = [
        ('toshkent', 'Toshkent'),
        ("bog'dod-rishton-buvayda", "Bog'dod-Rishton-Buvayda"),
        ("qo'qon", "Qo'qon"),
        ("uchko'prik", "Uchko'prik"),
    ]
    request_type = models.CharField(
        max_length=20,
        choices=REQUEST_TYPE_CHOICES,
        default='passenger_issue',
    )
    where = models.CharField(
        max_length=100,
        choices=WHERE_TYPE_CHOICES,
        default='toshkent',
    )
    whereTo = models.CharField(
        max_length=100,
        choices=WHERE_TYPE_CHOICES,
        default='toshkent',
    )
    Number = [
        ('1', '1'),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    ]
    yolovchiSoni = models.CharField(
        max_length=100,
        choices=Number,
        default='1',
    )
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.where} - {self.whereTo}"


class GetRequest(BaseModel):
    request = models.ForeignKey(Request, models.CASCADE)
    GETREQUEST_TYPE_CHOICES = [
        ('yolovchi_olish', 'Yolovchi olish'),
        ('pochta_olish', 'Pochta olish'),
    ]
    getrequest_type = models.CharField(max_length=50, choices=GETREQUEST_TYPE_CHOICES, default='yolovchi_olish')
    WHERE_TYPE_CHOICES = [
        ('toshkent', 'Toshkent'),
        ("bog'dod-rishton-buvayda", "Bog'dod-Rishton-Buvayda"),
        ("qo'qon", "Qo'qon"),
        ("uchko'prik", "Uchko'prik"),
    ]
    where = models.CharField(max_length=100, choices=WHERE_TYPE_CHOICES, default='toshkent')
    whereTo = models.CharField(max_length=100, choices=WHERE_TYPE_CHOICES, default='toshkent')

    def __str__(self):
        return f"{self.where} - {self.whereTo}"


class BalansToldirish(BaseModel):
    user = models.ForeignKey(UserProfile, models.CASCADE)
    summa = models.PositiveIntegerField()

    def __str__(self):
        return str(self.summa)


class BalansYechish(BaseModel):
    user = models.ForeignKey(UserProfile, models.CASCADE)
    summa = models.PositiveIntegerField()

    def __str__(self):
        return str(self.summa)