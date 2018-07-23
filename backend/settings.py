# coding: UTF-8
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


FLASK_PORT = int(os.environ.get('FLASK_PORT'))

DB_CONFIG = {
    'mysql': {
        'driver': 'mysql',
        'host': os.environ.get('DB_HOST'),
        'database': os.environ.get('DB_NAME'),
        'user': os.environ.get('DB_USER'),
        'password': os.environ.get('DB_PASSWORD'),
        'prefix': ''
    }
}