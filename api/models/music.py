from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='artists/', blank=True, null=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    author = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='albums/', blank=True, null=True)

    def __str__(self):
        return self.name

class Music(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.TimeField()
    spotify = models.TextField(max_length=250, blank=True, null=True)
    soundcloud = models.TextField(max_length=250, blank=True, null=True)
    deezer = models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name


