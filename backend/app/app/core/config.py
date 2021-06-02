import logging
import os

PG_URI_PATTERN = "postgresql://{user}:{password}@{host}:{port}/{db}"
SL_URI_PATTERN = "sqlite://"


class ConfigObject:
    APP_NAME = 'sort-met-out'
    LOG_LEVEL = 'info'

    def __getattribute__(self, attr):
        attr = attr.upper().strip()

        try:
            return os.environ[attr]
        except KeyError:
            return getattr(ConfigObject, attr)


Config = ConfigObject()


def get_db_uri(db_choice: str = 'sqlite'):
    db_choice = db_choice.lower()

    if db_choice == 'postgres':
        db_uri = PG_URI_PATTERN.format(user=Config.RDS_USERNAME,
                                       password=Config.RDS_PASSWORD,
                                       host=Config.RDS_HOSTNAME,
                                       port=Config.RDS_PORT,
                                       db=Config.RDS_DATABASE)
    elif db_choice == 'sqlite':
        db_uri = SL_URI_PATTERN

    else:
        raise Exception(f"`{db_choice}` DB is not supported")

    return db_uri

logging.basicConfig(format="[%(asctime)s] %(levelname)-7s [%(module)-11.11s] %(message)s")
logging.getLogger("sort-me-out").setLevel(Config.LOG_LEVEL.upper())
