from pydantic import BaseModel, HttpUrl


class URLRequest(BaseModel):
    original_url: HttpUrl
    expiry_days: int = 7
