from decouple import config

DB_NAME = config('DB_NAME', default='mydb')
DB_PASSWORD = config('DB_PASSWORD')
HOST = config('HOST', default='localhost')
USER = config('USER', default='myuser')
