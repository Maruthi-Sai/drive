from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from storage.models import DriveFolder

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    REQUIRED_FIELDS = ['username','first_name','last_name']
    USERNAME_FIELD = 'email'

    def get_username(self) -> str:
        return self.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_super_folder(sender, instance, created, **kwargs):
    if created:
        user = instance
        DriveFolder.objects.create(name=f'{user.id}_{user.first_name}', owner=user, is_folder=True, is_super=True)