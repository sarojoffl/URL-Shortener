# Django URL Shortener

## 🚀 Project Overview

A URL shortener built with Django that allows users to create short URLs, manage them, track clicks, and generate QR codes.

---

## 🚀 Features

- 🔐 User Authentication (Register, Login, Logout)
- 🔗 Create short URLs with unique short codes
- ⏳ Optional expiration time for URLs
- 📊 Click count tracking for each URL
- 📱 Auto-generated QR codes for short URLs
- 🛠️ Dashboard to view, edit, or delete URLs

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/sarojoffl/URL-Shortener.git
cd URL-Shortener
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Run development server
```bash
python manage.py runserver
```

---


## 📌 API Endpoint Documentation

| URL Pattern             | Description                     |
|-------------------------|---------------------------------|
| `/accounts/register/`   | Register a new user             |
| `/accounts/login/`      | Login user                      |
| `/accounts/logout/`     | Logout user                     |
| `/`                     | Dashboard – list all your URLs  |
| `/create/`              | Create a new short URL          |
| `/edit/<int:pk>/`       | Edit an existing short URL      |
| `/delete/<int:pk>/`     | Delete a short URL              |
| `/<str:short_code>/`    | Redirect short URL to original URL |

---

## 🧪 Testing Checklist

- ✅ Register, login, and logout
- ✅ Create short URL with unique code
- ✅ Edit and delete short URLs
- ✅ Click count increments correctly
- ✅ QR codes generated automatically
- ✅ Expiration dates work properly

---

## 🔒 Permissions

- Only authenticated users can create and manage URLs
- Users can only see and manage their own URLs

---

## 🧑‍💻 Author

Saroj
- 📧 sarojoffl@gmail.com
- 🌐 [github.com/sarojoffl](https://github.com/sarojoffl)
