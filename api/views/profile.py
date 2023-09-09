from api.models.profile import Profile
from api.serializers.profile import ProfileSerializer
from api.permissions.permissions import IsStaffOrReadOnly, IsAdminOrProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status

class ProfileViewSet (viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsStaffOrReadOnly]
    
class UserProfileViewSet (viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsAdminOrProfile]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        profile = self.get_object()
        if request.user != profile.user and not request.user.is_staff:
            return Response({'detail': 'You do not have permission to delete this profile'}, status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(profile)
        profile.user.delete()

        return Response({'detail': 'Account deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)