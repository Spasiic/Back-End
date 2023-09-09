from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from api.views.profile import ProfileViewSet, UserProfileViewSet
from api.authentication.authentication import RegisterView, LoginView, LogoutAPIView

r1 = routers.SimpleRouter()
r1.register('profiles', ProfileViewSet, basename='profiles')
r1.register('user/me', UserProfileViewSet, basename='getProfile')

urlpatterns = [
    path('', include(r1.urls)),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView().as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),     
]