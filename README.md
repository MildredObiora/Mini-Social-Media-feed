# 📸 Mini Social Media Feed — AltSchool Back‑End Project 1 - 

A bite‑sized social‑media service built with **Python + FastAPI**, showcasing user sign‑up, media posts, likes, and a personalized feed.  
Think of it as “Instagram Lite” for demo purposes — perfect for sharpening our back‑end chops.

![AltSchool](https://img.shields.io/badge/AltSchool-Backend-blue)
![Made with FastAPI](https://img.shields.io/badge/FastAPI-0.115.12-green)
![Python ≥ 3.10](https://img.shields.io/badge/Python-3.10%2B-yellow)

---

## ✨ What you can do

| Feature | Route sketch | Status |
|---------|--------------|--------|
| **Sign up / Sign in** | `POST /auth/register` & `POST /auth/login` | ✅ Done |
| **Create a post (text + file)** | `POST /posts/` (multipart) | 🔄 In progress|
| **See your feed** | `GET /feed` (`?user_id=` optional) | 🔄 In progress|
| **Like / unlike** | `POST /posts/{id}/like` & `DELETE /posts/{id}/like` | 🔄 In progress|
| **Like counters** | Auto‑updated on every like/unlike | 🔄 In progress|

> **Tech stack:** FastAPI • SQLModel (async) • PostgreSQL • JWT Auth • S3 / local file storage • Docker

---

## 🗂️ Suggested team lanes

| Lane              | Key tasks                                               |
|-------------------|---------------------------------------------------------|
| **User routes**   | Register, login, JWT auth middleware                    |
| **Post & files**  | Upload endpoint, file validation/storage                |
| **Feed service**  | Query & paginate posts, user filter                     |
| **Like engine**   | Like/unlike toggle, atomic counters, unit tests         |


---

## 🚀 Local quick‑start

```bash
# 1. Clone & move in
git clone [https://github.com/MildredObiora/Project1_Mini-Social-Media-Feed].git
cd Mini-Social-Media-Feed

# 2. Create env & install deps
python -m venv venv && source .venv/bin/activate
pip install -r requirements.txt

# 3. Copy env template & tweak
cp .env.example .env        # edit DB_URL, SECRET_KEY, AWS creds...

# 4. Run dev server
uvicorn app.main:app --reload

# 5. Open docs
# 👉 http://127.0.0.1:8000/docs
