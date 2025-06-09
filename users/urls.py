from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (CustomTokenObtainPairView, LogoutView, ProfileView,
                    RegisterView)

app_name = "user"
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
