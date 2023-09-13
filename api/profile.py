from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from api.models.profile import Profile
from rest_framework import viewsets
from api.permissions.permissions import IsStaffOrReadOnly, IsAdminOrOwner

# PROFILE SERIALIZERS:
# ----------------------------------------------------------------------------------------------
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')

class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'image', 'birth']
# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------

# PROFILE VIEWS:
# ----------------------------------------------------------------------------------------------
class ProfileViewSet (viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsStaffOrReadOnly]
    
class UserProfileViewSet (viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminOrOwner]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------