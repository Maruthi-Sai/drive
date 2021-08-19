from rest_framework import serializers
from storage.models import DriveFolder


class DriveFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriveFolder
        fields = ['id', 'name', 'file', 'is_folder', 'created_on', 'updated_on']
        
    def validate(self, data):
        is_folder = data.get('is_folder', None)
        file = data.get('file', None)
        name = data.get('name', None)
        if is_folder and name == None:
            raise serializers.ValidationError("Folder Name is Required")
        elif not is_folder and file==None:
            raise serializers.ValidationError("File is required")
        return data