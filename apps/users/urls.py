from django.urls import path
from . import api
urlpatterns = [
    path('auth/register/', api.RegisterAPI.as_view(), name="registration_api"),
    path('auth/login/', api.LoginAPI.as_view(), name="login_api"),
    path('auth/me/', api.UserAPI.as_view(), name="get_logged_in_user_api"),
]
