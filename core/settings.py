from decouple import config

DB_URI = config('DB_URI')
TEST_DB_URI = config('TEST_DB_URI')
FLASK_APP = config('FLASK_APP', default='app.py')
