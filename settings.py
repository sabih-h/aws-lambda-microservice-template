import json
import os
import sys

STAGE = os.getenv("STAGE") or "prod"

ON_MUSIC_EMAIL = os.getenv("ON_MUSIC_EMAIL")
ON_MUSIC_PASSWORD = os.getenv("ON_MUSIC_PASSWORD")

REDSHIFT_ACCESS_KEY_ID = os.getenv("REDSHIFT_ACCESS_KEY_ID")
REDSHIFT_SECRET_ACCESS_KEY = os.getenv("REDSHIFT_SECRET_ACCESS_KEY")

REDSHIFT_HOST = os.getenv("REDSHIFT_HOST")
REDSHIFT_USER = os.getenv("REDSHIFT_USER")
REDSHIFT_PASSWORD = os.getenv("REDSHIFT_PASSWORD")

config = json.load(open("config.json"))

REDSHIFT_DBNAME = config[STAGE]["REDSHIFT_DBNAME"]
REDSHIFT_SCHEMA = config[STAGE]["REDSHIFT_SCHEMA"]