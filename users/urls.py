from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from users.views import RegisterView, GetDetails, UpdateProfile, GetAllUsers, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('get-user/', GetDetails.as_view(), name='get-user'),
    path('upate-profile/', UpdateProfile.as_view(), name='update-profile'),
    path('get-all-users/', GetAllUsers.as_view(), name='get-all-users')
]
