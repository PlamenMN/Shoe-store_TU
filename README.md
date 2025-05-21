# 🛒 Shoe Store Django Project

This is a Django-based online shoe store project with core e-commerce functionalities such as product listings, user authentication, shopping cart, order processing, filtering, and admin tools.

---

## ✅ Prerequisites

- Python 3.8+
- pip
- virtualenv
- Git (optional)

---

## 🧪 Installation Guide

### 1. Create Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 2. Install Requirements

Using a `requirements.txt` file:

```txt
Django>=4.0
Pillow
```

Install with:

```bash
pip install -r requirements.txt
```

Or directly:

```bash
pip install django pillow
```

---

## 🏗️ Project Structure

```
shoestore/
├── manage.py
├── shoestore/         # Django settings
├── products/          # Product catalog app
├── accounts/          # User authentication
├── cart/              # Shopping cart
└── orders/            # Order handling
```

---

## ⚙️ Settings Configuration

### Add Apps in `settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'products',
    'accounts',
    'cart',
    'orders',
]
```

### Media & Static Files

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

Add in `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # your urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 🗃️ Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 👤 Create Superuser

```bash
python manage.py createsuperuser
```

---

## 🚀 Run Server

```bash
python manage.py runserver
```

---

## 🛠️ Development Tools (Optional)

```bash
pip install django-debug-toolbar
```

---

## 🔐 Environment Variables (Optional)

If using `python-decouple` or `django-environ`:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
```

---

## 📦 Features Summary

- Product listing with pagination, filtering, sorting
- User authentication
- Shopping cart and checkout
- Order history
- Admin panel for managing shoes
- Static and media files support
