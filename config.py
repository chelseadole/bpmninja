"""Config variables."""
import os

PROJECT_ID = os.environ.get('BPM_PROJECT_ID', None)
DATA_BACKEND = 'cloudsql'
CLOUDSQL_USER = os.environ.get('BPM_DB_USER', None)
CLOUDSQL_PASSWORD = os.environ.get('BPM_DB_PASSWORD', None)
CLOUDSQL_DATABASE = os.environ.get('BPM_DB_NAME', None)
BPM_CLOUDSQL_CONNECTION_NAME = os.environ.get('BPM_CLOUDSQL_CONNECTION_NAME', None)
