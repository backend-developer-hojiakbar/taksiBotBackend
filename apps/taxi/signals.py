from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Request, GetRequest
from apps.users.models import UserProfile


@receiver(post_save, sender=Request)
def update_user_balance(sender, instance, **kwargs):
    if instance.is_active:
        user = instance.user
        if instance.request_type == 'yolovchi_berish':
            user.balance += 5000 * int(instance.yolovchiSoni)
        elif instance.request_type == 'pochta_berish':
            user.balance += 3000
        user.save()


@receiver(post_save, sender=GetRequest)
def update_user_balance(sender, instance, **kwargs):
    if instance:
        user = instance.user
        if instance.getrequest_type == 'yolovchi_olish':
            user.balance -= 7500
        elif instance.getrequest_type == 'pochta_olish':
            user.balance -= 5000
        user.save()