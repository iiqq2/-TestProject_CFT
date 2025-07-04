from fastapi_users.authentication import CookieTransport,AuthenticationBackend, JWTStrategy
from conf import SECRET_AUTH


cookie_transport = CookieTransport(cookie_name="salary",cookie_max_age=3600)

SECRET = SECRET_AUTH

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)