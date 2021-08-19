from django.urls import path
from storage.api.views import (
    DriveFolderApiView,
)

urlpatterns = [
    path('folder/<str:folder_id>', DriveFolderApiView.as_view(), name='folder')
]