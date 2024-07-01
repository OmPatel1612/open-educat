from sqlalchemy import Column, Integer,VARCHAR, create_engine
from sqlalchemy.orm import declarative_base
db_url = "sqlite:///database.db"
engine = create_engine(db_url)
base = declarative_base()
class User(base):
    __tablename__="student"
    id=Column(Integer,primary_key=True)
    Name=Column(VARCHAR(30))
    Marks=Column(Integer)
base.metadata.create_all(engine)