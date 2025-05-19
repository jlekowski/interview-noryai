"""Docker compose specific settings"""

from weird_salads_site.settings import *  # noqa: F403

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django",
        "USER": "django",
        "PASSWORD": "F4B82F9D-730B-431E-B293-2ADDE2C2CE1F",
        "HOST": "postgres",
        "PORT": "5432",
    }
}
