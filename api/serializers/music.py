from rest_framework import serializers
from api.models.music import Artist, Album, Music

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    author_info = serializers.SerializerMethodField()
    author = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all(), write_only=True)

    def get_author_info(self, obj):
        return ArtistSerializer(obj.author).data

    class Meta:
        model = Album
        fields = ['id', 'author', 'name', 'image', 'author_info']

class MusicSerializer(serializers.ModelSerializer):
    album_info = serializers.SerializerMethodField()
    album = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all(), write_only=True)

    def get_album_info(self, obj):
        return AlbumSerializer(obj.album).data

    class Meta:
        model = Music
        fields = ['id', 'album', 'name', 'duration', 'album_info', 'spotify', 'soundcloud', 'deezer']




