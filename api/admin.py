from django.contrib import admin
from api.models.profile import Profile
from api.models.music import Artist, Album, Music
from api.models.misc import WishListEntry, Alarm

admin.site.register(Profile)

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Music)

admin.site.register(WishListEntry)
admin.site.register(Alarm)




