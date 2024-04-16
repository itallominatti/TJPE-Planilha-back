from django.urls import re_path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterUserView

urlpatterns = [
    re_path(r'^users/$', views.UserListCreate.as_view(), name='user-list-create'),
    re_path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^api/register/', RegisterUserView.as_view(), name='register')
]