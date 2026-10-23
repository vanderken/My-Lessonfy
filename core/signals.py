from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Collection, User, UserSettings

DEFAULT_COLLECTIONS = [
    ("Come back to this", "#FFD166"),
    ("Confusing", "#EF476F"),
    ("Study this", "#06D6A0"),
]


@receiver(post_save, sender=User)
def create_defaults_for_new_user(sender, instance, created, **kwargs):
    if not created:
        return
    UserSettings.objects.get_or_create(user=instance)
    for name, color in DEFAULT_COLLECTIONS:
        Collection.objects.get_or_create(
            user=instance,
            name=name,
            defaults={"color": color},
        )