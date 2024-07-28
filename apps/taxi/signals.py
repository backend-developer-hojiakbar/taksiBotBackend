from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Request
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