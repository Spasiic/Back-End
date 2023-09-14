from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from api.models.music import Music

class WishListEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    dttm_created = models.DateTimeField(default=timezone.now)
    time = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.music.name


