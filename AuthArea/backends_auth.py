from AuthArea.models import UserModel
import jwt
from rest_framework import authentication, exceptions
from django.conf import settings

class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None
        prefix, token = auth_data.decode('utf-8').split(' ')

        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms='HS256')

            user = UserModel.objects.get(email=payload['email'])
            return (user, token)
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed('Invalid Token, login')
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Expired Token, login')