from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///school.db")
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

def initialize_database():
    Base.metadata.create_all(bind=engine)
