import jwt
from datetime import datetime, timedelta
from django.conf import settings

ACCESS_TOKEN_EXPIRES_MINUTES = 60*24*30

def generateAccessToken(user):
    return jwt.encode(
        {
            "iss": "",
            "sub": str(user.id),
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES),
        },
        settings.SECRET_KEY,
        algorithm="HS256",
    )