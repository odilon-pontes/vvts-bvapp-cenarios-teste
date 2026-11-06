from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "apenas-para-fins-didaticos"
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = ["django.contrib.contenttypes", "django.contrib.auth"]
MIDDLEWARE = []
ROOT_URLCONF = "config.urls"
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Fortaleza"
USE_TZ = True
