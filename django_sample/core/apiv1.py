from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from auth import views as auth_views

app_name = 'apiv1'

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', auth_views.UserCreateView.as_view(), name='users')
]
