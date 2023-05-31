from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import register_user, logout_user, get_username

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),
    path('get_username/', get_username, name='get_username'),
]