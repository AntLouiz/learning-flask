import os.path
from decouple import config

DB_URI = config('DATABASE_URL')
TEST_DB_URI = config('TEST_DB_URI')
ENV = config('ENV', default='development')
FLASK_APP = config('FLASK_APP', default='app.py')
JWT_SECRET_KEY = config('JWT_SECRET_KEY', default='123')
JWT_BLACKLIST_ENABLED = config('JWT_BLACKLIST_ENABLED', default=True)
JWT_BLACKLIST_TOKEN_CHECKS = config('JWT_BLACKLIST_TOKEN_CHECKS', default=['access', 'refresh'])
UPLOAD_FOLDER = os.path.join(os.path.abspath('core'), 'uploads')
