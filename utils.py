import string
import random
from datetime import datetime, timedelta


def generate_short_code(length: int = 6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def get_expiry_date(days: int):
    return (datetime.now() + timedelta(days=days)).isoformat()
