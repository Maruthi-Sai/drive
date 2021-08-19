from django.db import models
from django.conf import settings
from django.db.models.fields import files

# Create your models here.


def upload_file(instance,filename):
    return f'uploads/{instance.owner.id}/{filename}'


class DriveFolder(models.Model):
    name            = models.CharField(max_length=255, null=True)
    file            = models.FileField(upload_to=upload_file, max_length=255, null=True)
    owner           = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='folder', on_delete=models.CASCADE)
    parent          = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    is_folder       = models.BooleanField(default=False)
    is_super        = models.BooleanField(default=False)
    created_on      = models.DateTimeField(auto_now_add=True)
    updated_on      = models.DateTimeField(auto_now=True)

    def str(self):
        return self.name