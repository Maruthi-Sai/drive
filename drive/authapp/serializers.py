from django.db import models
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import Serializers
from .models import User


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email','username','password','first_name','last_name',)