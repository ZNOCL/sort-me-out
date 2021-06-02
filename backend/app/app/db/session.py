from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import get_db_uri

# engine = create_engine(
#     get_db_uri(), connect_args={"check_same_thread": False}
# )

engine = create_engine(get_db_uri(), pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


