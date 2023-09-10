from api.models.music import Artist, Album, Music
from api.serializers.music import ArtistSerializer, AlbumSerializer, MusicSerializer
from rest_framework import viewsets

class ArtistViewSet (viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet (viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class MusicViewSet (viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer