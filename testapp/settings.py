SECRET_KEY = 'test_*@^1w+=ttwytvz%#rga7f&+8oi_up#vk5ck68z$!s*4&-cd$t5'

DATABASES = {
    'default': {
        'NAME': ':memory:',
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = (
    'main',
    'exceptionstest',
    'smoketest',
)

MIDDLEWARE_CLASSES = []

ROOT_URLCONF = 'urls'
