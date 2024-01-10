import uuid

import jwt
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class AnonymousUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            user_id = request.session.get("user_id")
            if not user_id:
                user_id = str(uuid.uuid4())
                request.session["user_id"] = user_id

            # Generate a custom JWT token with the unique identifier
            encoded_jwt = jwt.encode(
                {"user_id": user_id}, settings.SECRET_KEY, algorithm="HS256"
            )
            request.session["jwt_token"] = encoded_jwt

            try:
                decoded_data = jwt.decode(
                    encoded_jwt, settings.SECRET_KEY, algorithms=["HS256"]
                )
                request.user_id = decoded_data.get("user_id")
            except jwt.ExpiredSignatureError:
                # Handle the token being expired
                pass
            except jwt.InvalidTokenError:
                # Handle the token being invalid
                pass
