import secrets
import string

available_chars = string.ascii_lowercase + string.digits


def generate_alias(length: int = 3) -> str:
    return "".join(secrets.choice(available_chars) for _ in range(length))
