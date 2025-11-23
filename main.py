from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from datetime import datetime
from . import database, schemas, utils

app = FastAPI(title="URL Shortener (Python + FastAPI)")

# Initialize DB
database.create_table()


@app.post("/shorten")
def shorten_url(request: schemas.URLRequest):
    short_code = utils.generate_short_code()

    # Ensure uniqueness
    while database.get_url(short_code):
        short_code = utils.generate_short_code()

    expiry_date = utils.get_expiry_date(request.expiry_days)

    database.insert_url(request.original_url, short_code, expiry_date)

    return {
        "short_url": f"http://localhost:8000/{short_code}",
        "expires_on": expiry_date
    }


@app.get("/{short_code}")
def redirect(short_code: str):
    data = database.get_url(short_code)

    if not data:
        raise HTTPException(status_code=404, detail="Short URL not found")

    original_url, expiry = data

    if datetime.fromisoformat(expiry) < datetime.now():
        raise HTTPException(status_code=410, detail="Short URL expired")

    return RedirectResponse(original_url)
