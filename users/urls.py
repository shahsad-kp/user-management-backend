from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserListView, UserCreateView, UserUpdateSelfView, UserUpdateAdminView, UserDeleteAdminView, \
    UserRetrieveView, UserRegistrationView, UserLoginView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/update/', UserUpdateSelfView.as_view(), name='user-update-self'),
    path('users/update/<int:pk>/', UserUpdateAdminView.as_view(), name='user-update-admin'),
    path('users/delete/<int:pk>/', UserDeleteAdminView.as_view(), name='user-delete-admin'),
    path('users/retrieve/', UserRetrieveView.as_view(), name='user-retrieve'),
    path('users/register/', UserRegistrationView.as_view(), name='user-register'),
    path('users/login/', UserLoginView.as_view(), name='user-login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
