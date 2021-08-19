from rest_framework import fields, serializers
from storage.models import DriveFolder, DriveFile


class DriveFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriveFolder
        fields = '__all__'


class DriveFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriveFile
        fields = '__all__'