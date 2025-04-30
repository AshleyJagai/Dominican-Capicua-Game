# Development Log: Capicúa Vivo

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
- Created games app for managing Capicua matches and game rooms
- Registered games app in backend/settings.py

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
├── games/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── manage.py
├── venv/ (ignored)
├── .gitignore
├── README.md
└── DEVLOG.md (this file)
```

### 🛠️ API Development

### 🎯 GameRoom Model & Migrations 
- Created `GameRoom` model in `games/models.py`
- Added many-to-many relationship with `User`
- Ran `makemigrations` and `migrate` to apply changes

### 🎯 Create Room API
- Built `create_game_room` view in `games/views.py`
- Allowed creation of GameRoom with unique `room_name`
- Added POST route to `games/urls.py`
- Tested via `curl`

### 🎯 Join Room API Setup
- Built `join_game_room` view with POST support
- Player joins room by name (if under 4 members)
- Added logic to prevent duplicate joins
- Route added to games/urls.py

## 🗓️ April 28-30, 2025

### 🎨 Design System & Branding

### 🎯 Style Guide
- Created full Airbnb-inspired visual style guide
- Defined:
    - Font: Noto Sans (Google Fonts)
    - Colors: Deep Blue, Refined Red, Mambo Yellow, Fresh Green, White/Tan
    - Button states, spacing system, hover effects, elevation/shadows
    - Tile visual styling and size guidance
    - Created layout specs for buttons, typography hierarchy, and responsiveness

### 🎯 Branding Finalized
- App name: Capicúa Vivo
- Brand identity keywords:
    - Authentic & Cultural
    - Warm & Lively
    - Nostalgic & Competitive
- Created:
    - Brand board with typography, logo, colors, iconography
    - Logo asset on procreate
    - Title asset on procreate
    - Double-six domino asset on procreate
    - Tile design template (off-white background, black dots, shadow)


### 🖥️ UI/UX Wireframes & Screens

### 🎯 Login Screen
- Fields: email/username + password
- Password visibility toggle (eye icon)
- Login button with hover state
- Forgot password link
- Language switch (EN/ES)
- Responsive layout ready for mobile/tablet
- Error message display pattern defined

### 🎯 Lobby Screen
- Welcome banner with user greeting
- Create Room / Join Room buttons (primary style)
- Active rooms list with live player count and join buttons
- User avatar placeholder
- Logout + language switch integration

### 🎯 Settings Screen
- Audio toggle (on/off)
- Theme switcher (light/dark)
- Language switch moved here for cleaner UI
- Chat mute option
- Logout button
- All toggles designed with consistent UI spec (green active, gray inactive)



