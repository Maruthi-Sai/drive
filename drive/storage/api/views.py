from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from storage.api.serializers import DriveFolderSerializer
from storage.models import DriveFolder

class DriveFolderApiView(APIView):
    authentication_classes  = []
    permission_classes      = []

    def get(self, request, folder_id):
        child_folders = DriveFolder.objects.filter(parent=folder_id)
        folder_serializer = DriveFolderSerializer(child_folders, many=True)
        return Response(folder_serializer.data, status=status.HTTP_200_OK)