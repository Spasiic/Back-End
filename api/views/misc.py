from api.models.misc import WishListEntry
from api.serializers.misc import WishListEntrySerializer
from api.permissions.permissions import IsAdminOrOwner
from rest_framework import viewsets

class WishListEntryViewSet (viewsets.ModelViewSet):
    queryset = WishListEntry.objects.all()
    serializer_class = WishListEntrySerializer
    permission_classes = [IsAdminOrOwner]
