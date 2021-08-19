from rest_framework import serializers
from storage.models import DriveFolder


class DriveFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriveFolder
        fields = '__all__'
        