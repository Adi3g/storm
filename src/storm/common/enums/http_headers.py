from enum import Enum

class HttpHeaders(Enum):
    CONTENT_TYPE = "Content-Type"
    AUTHORIZATION = "Authorization"
    ACCEPT = "Accept"
    USER_AGENT = "User-Agent"
    COOKIE = "Cookie"
    SET_COOKIE = "Set-Cookie"
    CACHE_CONTROL = "Cache-Control"
    CONTENT_LENGTH = "Content-Length"
    HOST = "Host"
    ORIGIN = "Origin"
    REFERER = "Referer"
    CONNECTION = "Connection"
    ACCEPT_ENCODING = "Accept-Encoding"
    X_FORWARDED_FOR = "X-Forwarded-For"
    X_REAL_IP = "X-Real-IP"
    ACCEPT_LANGUAGE = "Accept-Language"
    ACCESS_CONTROL_ALLOW_ORIGIN = "Access-Control-Allow-Origin"
    ACCESS_CONTROL_ALLOW_METHODS = "Access-Control-Allow-Methods"
