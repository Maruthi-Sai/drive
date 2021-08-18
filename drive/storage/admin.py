from django.contrib import admin
from .models import DriveFolder, DriveFile

# Register your models here.


admin.site.register(DriveFolder)
admin.site.register(DriveFile)