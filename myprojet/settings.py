"""
Django settings for myprojet project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import firebase_admin
from firebase_admin import credentials,firestore
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+ba1k(kyw%fii$%6v*-r2iq98uz_xmyzew@%ug17%zlf0i)=c1"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']
CORS_ALLOW_ALL_ORIGINS = True # added
CORS_ALLOW_CREDENTIALS = True # added
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'corsheaders', # added
    "myapp" , # added
    'rest_framework', # added

]
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        
    ]
}
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware', # added
]

ROOT_URLCONF = "myprojet.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR,"templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "myprojet.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "krishna"),
        "USER": os.getenv("DB_USER", "postgres"),
        "PASSWORD": os.getenv("DB_PASSWORD", "Radhe"),
        "HOST": os.getenv("DB_HOST", "db"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}


# Your credentials dictionary
cred = {
    "type": "service_account",
    "project_id": "django-95298",
    "private_key_id": "ef967fe6c4e8d731ab8c75e9d56f876f04796bae",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCkP9+mwsbeNSWh\n0kVH/m8kwypKm0DD6pU9Val3bkP73mGYckN/KdJ8Plz2OpV/H+EXcJruN03OS107\n+X1NRntJnPuN/kd1ZVOCZTFoWRCNLjUQukvhqQZSjNORyeOlY32A8kVKTpjWEuUc\nhobfLdKWNFkN8/H4/8px0RyXtsHv8vTm1kAKyNv138aDABhZ5yN6afykW6Ke2qob\n33ItDvUq75/d14o2UziPT5VP4SydUj81sAmV0fpgfGkmUhUIoT0nkeZPo3GWXIOU\ner5GzaX8XYTxUuxaJVsjEAcmLtQ/XMLjAkyn4w0iCxhZt+IN58ryaGzuC2EtABnz\nWxSwfOcNAgMBAAECggEAFr2gN8zCb3wQxoegH4Bm/4JE/fjiXe3B9XDBip9Z6sqm\nnQ5+8WGHOrwAr3e7gJMXnWDyFnbSPzR4h2f61QLj6XSCcK2q06Jwjj53+YBRVha2\ncqc0f90g2reUSFxZOCoe84Y3mTrqFsOddJZcoJRN0o2TYebrUuQJcbo32PqM/e1e\n2YlnauUTdGZzKj/iNlkhVwt02vH8FCqAuEl28idW86HcJ7WaeHPCDXoV7fkvPIsc\nC3XhZ9y/PiFKiZ+uasFy5ej+4mc1mewHby2D24yY4DVod12EBGAF5iPACiyJhVKT\nD/ydkcQPuud2kgKXOGfBSf7BuhKo89Du9lhyVFGnkQKBgQDbT23e+Ap/ERNG/HWB\nQ+eNGpIazBZa3m56K1ROftNPZ2hUsqOEWTvqk5CrzFA6Bfg5oFnatYUXMiHjm/Te\nDPCoXSfwmHncQuAT3TqmRv7oWwi+837b008VuObIt71PDfE2quCv7iB+REO73Mq6\nvu7ekRIfRF0rhyWwZ+gyjO5dEQKBgQC/ulCBSMlJH70u/gQc36oC5EgztVVBXwc1\nTIx8rtpJpCkhfu7Pi2SjEzGxgHzcZSLrOR+tyy96rPPbHuhjvPuITaEzOvNxI4/r\n9D+0btBbqkfla6C4QfBo+RBnctXiKOA4RquSzEOiQcEHMzjFzbiZRWIwYdwcn5YD\n+Bm+5m0aPQKBgBJjY4v5ci/bR6mBC30uK2EKZEu45vrxgYPe1C/MtH0I55eKbulu\n7fYqL0woUmW7EGgMiNwssh8SxgKmle50WU1Umj+zGSydstoXh45fj4n98ArKsc1O\nt2fT3A3iUg4p1hrGUxaNOc48fQ1oYtsrnS2uLj3O5pz6tO9IlxB9/pJxAoGAKJmV\nrqrxJPD5qNfVmx+p6s7Yk0qU8TDkX98D6OtGAk4m/5bXj0+fUgEghswEpM8t483G\n7ZCXT00Mnpwe7e/4+9YkiqqzHoQ/V+HzE4xbxu16KBTwhdRAypnjZWSl8ixhvskI\nUB+9OsDd1V59aTW1H4/XyRMP/2ez5sdE/G3jMKkCgYAW0/b7BJL/YeOlUg5VUIci\n/946kib4HbdF86hJwY6yekyYGv4AV++deoSNO4WYYSf25Hok2ICrttaSHlENeDt/\nUasqaRGUiDXDcoBRAgZu/6RBVTKDikjKEAvNALpKXlV+54rkRInPs2qiWbOXuCEl\nU0XLdsl7Uj1ST4jB7Zbt+w==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-ibal6@django-95298.iam.gserviceaccount.com",
    "client_id": "106885300725280014587",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ibal6%40django-95298.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

# Initialize Firebase
firebase_admin.initialize_app(credentials.Certificate(cred), {
    'databaseURL': "https://django-95298-default-rtdb.firebaseio.com/"
})
# .==================================================================================

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# REST Framework and OAuth Toolkit settings=====================================================
