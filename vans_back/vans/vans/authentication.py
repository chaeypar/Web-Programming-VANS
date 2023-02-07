import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from user.models import User


class JWTAuthentication(BaseAuthentication):
    
    # 인증실패: None
    # 인증성공: (user, token)
    def authenticate(self, request):
        auth = request.META.get("HTTP_AUTHORIZATION")
        if not auth:
            return None
        try:
            auth = auth.split(' ')
            if auth[0] != 'Bearer':
                return None
            token = auth[1]
            access_data = jwt.decode(
				token,
				settings.SECRET_KEY,
				algorithms="HS256",
			)
            id = access_data.get('sub')
            user = User.objects.get(id=id)
            return (user, None)
        except:
            return None
    
