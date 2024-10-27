#Import Serializer Class
from rest_framework import serializers

#Import Models
from django.contrib.auth.models import User, Group
from Accounts.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # Get the token from the parent class
        token = super().get_token(user)

        # Collect user permissions
        user_permissions = [perm.codename for perm in user.user_permissions.all()]

        # Collect group permissions
        group_permissions = []
        for group in user.groups.all():
            group_permissions.extend([perm.codename for perm in group.permissions.all()])

        # Combine user and group permissions
        all_permissions = list(set(user_permissions + group_permissions))

        # Add custom claims to the token
        token['permissions'] = all_permissions
        token['user'] = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
        }
        token['groups'] = [group.name for group in user.groups.all()]

        return token