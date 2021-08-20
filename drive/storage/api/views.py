from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status, authentication, permissions
from storage.api.serializers import DriveFolderSerializer
from storage.models import DriveFolder
from django.shortcuts import get_object_or_404

class DriveFolderApiView(APIView):

    def get(self, request, folder_id, format=None):
        folder = get_object_or_404(DriveFolder, pk=folder_id)
        child_folders = DriveFolder.objects.filter(parent=folder)
        folder_serializer = DriveFolderSerializer(child_folders, many=True)
        return Response(folder_serializer.data, status=status.HTTP_200_OK)

    def post(self, request, folder_id, format=None):
        folder = get_object_or_404(DriveFolder, pk=folder_id)
        serializer = DriveFolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user,parent=folder)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, folder_id, format=None):
        id = request.data['id']
        folder = get_object_or_404(DriveFolder, pk=id)
        if folder.is_folder:
            serializer = DriveFolderSerializer(folder, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, folder_id, format=None):
        id = request.data['id']
        folder = get_object_or_404(DriveFolder, pk=id)
        folder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)