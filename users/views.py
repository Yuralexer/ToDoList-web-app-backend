from rest_framework import generics, status, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import UserProfileSerializer, UserRegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer


class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")
        if refresh_token:
            request.data["refresh"] = refresh_token
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            access_token = response.data.pop("access")
            refresh_token = response.data.pop("refresh")
            response.set_cookie(
                key="access_token",
                value=access_token,
                httponly=True,
                samesite="Lax",
            )
            response.set_cookie(
                key="refresh_token",
                value=access_token,
                httponly=True,
                samesite="Lax",
            )
            return response
        
class LogoutView(views.APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response
