import os
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'shindpfla.mysql.pythonanywhere-services.com',
        'NAME': 'shindpfla$epost_db',
        'USER': 'shindpfla',
        'PASSWORD': 'mysql1111',

        'OPTIONS': { 'charset': 'utf8mb4', },
    }
}