import base64
import os
import hmac
import hashlib

from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

SECRET = os.getenv("SECRET", "super-secret-key")

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return password_context.verify(plain, hashed)

def generate_token(user_id: int):
    expiration = datetime.now(timezone.utc) + timedelta(minutes=480) # token dura 8 horas
    payload = f"{user_id}:{expiration.isoformat()}"
    signature = hmac.new(SECRET.encode(), payload.encode(), hashlib.sha256).hexdigest()
    return base64.urlsafe_b64encode(f"{payload}:{signature}".encode()).decode()

def decode_token(token):
    try:
        decoded = base64.urlsafe_b64decode(token.encode()).decode()
        user_id, expiration, signature = decoded.split(":")
        payload = f"{user_id}:{expiration}"
        expected = hmac.new(SECRET.encode(), payload.encode(), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(signature, expected):
            return None
        if datetime.now(timezone.utc) > datetime.fromisoformat(expiration):
            return None
        return int(user_id)
    except (ValueError, TypeError):
        return None
