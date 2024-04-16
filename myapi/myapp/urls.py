from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^users/$', views.UserListCreate.as_view(), name='user-list-create'),
]