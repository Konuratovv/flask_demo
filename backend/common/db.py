from sqlalchemy import create_engine
from models import BaseModel

engine = create_engine('sqlite:///database.db', echo=True)

def create_db_and_tables():
    BaseModel.metadata.create_all(engine)
    