# signals.py
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import Profile, Community

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         profile = Profile.objects.create(user=instance)
#         # Find or create the community based on the user's location
#         community, _ = Community.objects.get_or_create(name=profile.location)
#         profile.community = community
#         profile.save()
