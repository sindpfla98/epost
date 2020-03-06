import os
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'sindpflaBirdview.mysql.pythonanywhere-services.com',
        'NAME': 'sindpflaBirdview$epost_db',
        'USER': 'sindpflaBirdview',
        'PASSWORD': 'mysql1111',

        'OPTIONS': { 'charset': 'utf8mb4', },
    }
}