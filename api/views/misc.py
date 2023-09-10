from api.models.misc import WishListEntry, Alarm
from api.serializers.misc import WishListEntrySerializer, AlarmSerializer
from api.permissions.permissions import IsAdminOrOwner
from rest_framework import viewsets

class WishListEntryViewSet (viewsets.ModelViewSet):
    queryset = WishListEntry.objects.all()
    serializer_class = WishListEntrySerializer
    permission_classes = [IsAdminOrOwner]

class AlarmViewSet (viewsets.ModelViewSet):
    queryset = Alarm.objects.all()
    serializer_class = AlarmSerializer
    permission_classes = [IsAdminOrOwner]
