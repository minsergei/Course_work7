from django.urls import path
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from users.views import UserRetrieveAPIView, UserCreateAPIView, UserUpdateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = UsersConfig.name

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('register/', UserCreateAPIView.as_view(permission_classes=(AllowAny,)), name='register'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),

    path("user/<int:pk>/", UserRetrieveAPIView.as_view(), name="user_detail"),
    path("user/update/<int:pk>/", UserUpdateAPIView.as_view(), name="user_update"),
]
