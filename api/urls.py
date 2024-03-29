from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from api.profile import ProfileViewSet, UserProfileViewSet
from api.music import ArtistViewSet, AlbumViewSet, MusicViewSet
from api.misc import WishListEntryViewSet
from api.authentication.authentication import RegisterView, LoginView, LogoutAPIView

r1 = routers.SimpleRouter()
# Authentication
r1.register('profiles', ProfileViewSet, basename='profiles')
r1.register('user/me', UserProfileViewSet, basename='getProfile')

#music
r1.register('artists', ArtistViewSet, basename='artists')
r1.register('albums', AlbumViewSet, basename='albums')
r1.register('musics', MusicViewSet, basename='musics')

#misc
r1.register('wishlistentries', WishListEntryViewSet, basename='wishlistsentries')

urlpatterns = [
    path('', include(r1.urls)),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView().as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()), 
]