from rest_framework import serializers
from api.models.misc import WishListEntry, Alarm

class WishListEntrySerializer(serializers.ModelSerializer):

    def validate(self, data):
        # Get the request user and the instance user
        request_user = self.context['request'].user
        instance_user = data.get('user')

        # Check if the request user is an admin or the instance user is the same as the request user
        if not request_user.is_staff and request_user != instance_user:
            raise serializers.ValidationError("You do not have permission to modify this entry.")

        return data

    class Meta:
        model = WishListEntry
        fields = '__all__'

    

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
    
    