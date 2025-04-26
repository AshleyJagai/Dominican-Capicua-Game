# Development Log: Dominican Capicua Game

---

## 🗓️ April 25-26, 2025

### ➡️ Project Setup
- Created main project folder `dominican-capicua/`
- Created and activated a Python virtual environment `venv/`
- Upgraded pip to the latest version for better package management
- Installed Django and Django Channels for web and real-time socket support
- Started Django project inside the folder with `django-admin startproject backend .`

### ➡️ Git & GitHub Setup
- Initialized Git repository locally with `git init`
- Created remote GitHub repository `Dominican-Capicua-Game`
- Linked local project to GitHub remote with `git remote add origin`
- Created `.gitignore` to exclude `venv/`, `db.sqlite3`, and cache files
- Resolved remote README conflict by merging and cleaning `.gitignore`
- Successfully pushed local backend code and setup to GitHub

### ➡️ Django Apps Setup
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


## 📝 Notes:
- Django Channels will handle WebSocket communication for real-time gameplay.
- Players (users) and game rooms (games) will be separate apps for cleaner architecture.
- Early commits focus on backend scaffolding before frontend or game logic begins.
- Following clean Git practices: small commits, meaningful messages, pushing after milestones.


---

*(Next major step: Create `games` app for managing Capicua matches and real-time gameplay.)*


