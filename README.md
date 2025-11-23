# URL Shortener Service (Python + FastAPI)

A lightweight URL shortening service built with Python and FastAPI.  
Generates unique short codes using hashing logic, stores mappings in SQLite,  
and redirects users to the original URL.

---

## 🚀 Features
- Shorten long URLs
- Auto-expiry support
- Fast redirects via hash lookup
- Collision-safe short code generation
- Input validation using Pydantic
- Clean REST API

---

## 📂 Project Structure
fastapi-url-shortener/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ ├── utils.py
│── requirements.txt
│── README.md
