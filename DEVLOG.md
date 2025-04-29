# Development Log: Dominican Capicua Game

---

## 🗓️ April 25-26, 2025

### 🎯 Project Setup
- Created main project folder `dominican-capicua/`
- Created and activated a Python virtual environment `venv/`
- Upgraded pip to the latest version for better package management
- Installed Django and Django Channels for web and real-time socket support
- Started Django project inside the folder with `django-admin startproject backend .`

### 🎯 Git & GitHub Setup
- Initialized Git repository locally with `git init`
- Created remote GitHub repository `Dominican-Capicua-Game`
- Linked local project to GitHub remote with `git remote add origin`
- Created `.gitignore` to exclude `venv/`, `db.sqlite3`, and cache files
- Resolved remote README conflict by merging and cleaning `.gitignore`
- Successfully pushed local backend code and setup to GitHub

### 🎯 Django Apps Setup
- Created `users` app using `python manage.py startapp users`
- Registered `users` app in `backend/settings.py` under `INSTALLED_APPS`

## 📂 Project Structure (after Setup)
```
Dominican-Capicua/
├── backend/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── migrations/
├── manage.py
├── venv/ (ignored)
├── .gitignore
├── README.md
└── DEVLOG.md (this file)
```

### 🎯 Django Apps Setup 
- Created `games` app for managing Capicua matches and game rooms
- Registered `games` app in backend/settings.py

### 🎯 Models Setup
- Created `GameRoom` model in `games` app to manage match rooms
- Added many-to-many relationship with users
- Migrated database to create GameRoom table

### 🎯 Join Room API Setup
- Built API endpoint to allow players to join an existing GameRoom
- Made player limit of 4 per room
- Updated games/urls.py to add join route

