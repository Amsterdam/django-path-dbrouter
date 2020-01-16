import os
from dataservices import dsns_from_env
import dj_database_url


def dbconfig_from_env(db_env_name="DATABASES"):
    database_config = {}
    for db_name, dsn in dsns_from_env(db_env_name):
        database_config[db_name] = dj_database_url.parse(dsn)
    return database_config
