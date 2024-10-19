import base64
import os

from flask import request
# from flask_jwt_extended import decode_token
from jose import jwt


def bdv_basic_auth(username, password):
    if not username and not password:
        return {}
    try:
        if username == "admin" and password == "password":
            return {"access_token": username}
    except Exception:
        pass
    return None


def decode_auth_header(auth_header):
    base64_credentials = auth_header.split(" ")[1]
    decoded_credentials = base64.b64decode(base64_credentials).decode("utf-8")
    username, password = decoded_credentials.split(":")
    return username, password


def decode_jwt(token):
    try:
        jwt_secret_key = os.environ.get("JWT_SECRET_KEY")
        decoded_token = jwt.decode(token, jwt_secret_key, algorithms=["HS256"])
        return decoded_token
    except Exception as e:
        return None


def bdv_bearer_auth(token):
    if not token:
        return None
    try:
        token = token.replace("Bearer ", "")
        decoded = decode_jwt(token)
        return decoded
    except Exception:
        return None
