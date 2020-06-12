from django.urls import path

from auth import views as auth_views

app_name = 'apiv1'

urlpatterns = [
    path('users/', auth_views.UserCreateView.as_view(), name='users')
]
