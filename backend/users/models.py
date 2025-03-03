# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

# Predefined locations
LOCATIONS = [
    ('Freetown', 'Freetown'),
    ('Bo', 'Bo'),
    ('Kenema', 'Kenema'),
    ('Makeni', 'Makeni'),
    ('Koidu', 'Koidu'),
]

class Community(models.Model):
    name = models.CharField(max_length=100, choices=LOCATIONS, unique=True)

    def __str__(self):
        return self.name
    
    
class CustomUser(AbstractUser):
    community = models.ForeignKey(Community, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.username
    
    
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE) 
#     location = models.CharField(max_length=100, choices=LOCATIONS)
#     community = models.ForeignKey(Community, on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return f'{self.user.username} - {self.location} ({self.community})'

