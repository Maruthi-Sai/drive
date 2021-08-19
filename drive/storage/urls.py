from django.urls import path, include


app_name='storage'

urlpatterns = [
    path('api/', include('storage.api.urls')),
]