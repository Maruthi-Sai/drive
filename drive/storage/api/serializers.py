from rest_framework import serializers
from storage.models import DriveFolder


class DriveFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriveFolder
        fields = ['id', 'name', 'file', 'is_folder', 'created_on', 'updated_on']
        