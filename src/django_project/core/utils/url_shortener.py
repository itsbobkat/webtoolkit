import secrets
import string
from urllib.parse import urlparse

available_chars = string.ascii_lowercase + string.digits


def generate_alias(length: int = 3) -> str:
    return "".join(secrets.choice(available_chars) for _ in range(length))


def is_http_url(url: str, allowed_schemes: list[str] | None = None) -> bool:
    if not allowed_schemes:
        allowed_schemes = ["https", "http"]
    try:
        result = urlparse(url)
        return all([result.scheme in allowed_schemes, result.netloc])
    except:
        return False
