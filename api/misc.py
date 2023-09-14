from django.utils import timezone
from rest_framework import serializers
from api.models.misc import WishListEntry
from api.models.music import Music
from api.music import MusicSerializer    
from api.permissions.permissions import IsAdminOrOwner
from rest_framework import viewsets

# MISC SERIALZIERS:
# --------------------------------------------------------------------------------------------
class WishListEntrySerializer(serializers.ModelSerializer):
    music_info = serializers.SerializerMethodField()
    music = serializers.PrimaryKeyRelatedField(queryset=Music.objects.all(), write_only=True)

    def get_music_info(self, obj):
        return MusicSerializer(obj.music).data

    def validate(self, data):
        # Get the request user and the instance user
        request_user = self.context['request'].user
        instance_user = data.get('user')
        time = data.get('time')

        # Check if the request user is an admin or the instance user is the same as the request user
        if not request_user.is_staff and request_user != instance_user:
            raise serializers.ValidationError("You do not have permission to modify this entry.")
        if time and time <= timezone.now():
            raise serializers.ValidationError("Do you have a time machine, my friend?")
        return data
    class Meta:
        model = WishListEntry
        fields = ['user', 'music', 'music_info', 'time', 'dttm_created']
        read_only_field = ['dttm_created']
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

# MISC VIEWS:
# --------------------------------------------------------------------------------------------
class WishListEntryViewSet (viewsets.ModelViewSet):
    queryset = WishListEntry.objects.all()
    serializer_class = WishListEntrySerializer
    permission_classes = [IsAdminOrOwner]
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------