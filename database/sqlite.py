from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def get_active_session():
    # todo should we refactor?
    db_session = sessionmaker(bind=create_engine('sqlite:///tiny.db'))
    db_active_session = db_session()
    return db_active_session
