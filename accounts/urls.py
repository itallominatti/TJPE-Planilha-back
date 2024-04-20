from accounts.views.signin import SignIn
from django.urls import path


urlpatterns = [
    path('signin/', SignIn.as_view())
]