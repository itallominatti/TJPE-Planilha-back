from accounts.views.base import Base
from accounts.auth import Authentication
from accounts.serializers import UserSerializer

from rest_framework.response import Response
from rest_framework.simplejwt.tokens import RefreshToken

class SignIn(Base):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        token = RefreshToken.for_user(user)

        user = Authentication,SignIn(self, email, password)
        enterprise = self.get_enterprise_user(user.id)
        serializer = UserSerializer(user)

        return Response({
            "user": serializer.data,
            "enterprise": enterprise,
            "refresh": token.refresh,
            "access_token": token.access_token
        })







