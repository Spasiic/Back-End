from rest_framework import serializers
from api.models.misc import WishListEntry, Alarm
from api.models.music import Music
from api.serializers.music import MusicSerializer

class WishListEntrySerializer(serializers.ModelSerializer):

    def validate(self, data):
        # Get the request user and the instance user
        request_user = self.context['request'].user
        instance_user = data.get('user')

        # Check if the request user is an admin or the instance user is the same as the request user
        if not request_user.is_staff and request_user != instance_user:
            raise serializers.ValidationError("You do not have permission to modify this entry.")

        return data

    music_info = serializers.SerializerMethodField()
    music = serializers.PrimaryKeyRelatedField(queryset=Music.objects.all(), write_only=True)

    def get_music_info(self, obj):
        return MusicSerializer(obj.music).data

    class Meta:
        model = WishListEntry
        fields = ['user', 'music', 'music_info', 'dttm_created']
        read_only_fields = ['music_info', 'dttm_created']


class AlarmSerializer(serializers.ModelSerializer):

    def validate(self, data):
        # Get the request user and the instance user
        request_user = self.context['request'].user
        instance_user = data.get('wishlist_entry').user

        # Check if the request user is an admin or the instance user is the same as the request user
        if not request_user.is_staff and request_user != instance_user:
            raise serializers.ValidationError("You do not have permission to modify this entry.")

        return data
    
    class Meta:
        model = Alarm
        fields = '__all__'
    
    