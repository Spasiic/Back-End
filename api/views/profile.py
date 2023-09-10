from api.models.profile import Profile
from api.serializers.profile import ProfileSerializer
from api.permissions.permissions import IsStaffOrReadOnly, IsAdminOrOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status

class ProfileViewSet (viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsStaffOrReadOnly]
    
class UserProfileViewSet (viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminOrOwner]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
