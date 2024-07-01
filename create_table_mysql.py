from sqlalchemy import create_engine, Column, Integer,String,Text,VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
URL_DATABASE="mysql+pymysql://root:admin@localhost:3306/crud_database" 
engine=create_engine(URL_DATABASE)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()

# Define your table's schema by creating a class
class Student_marks(Base):
    __tablename__="student_marks"
    name= Column(Text())
    marks=Column(Integer)
    id=Column(VARCHAR(255),primary_key=True)
    
    
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()

def enter_data_in_table(name,marks,id):
    student_data=Student_marks(name=name,marks=marks,id=id)
    session.add(student_data)
    session.commit()
    session.close()
    

enter_data_in_table("sachin",67,1)
enter_data_in_table("himal",70,2)
enter_data_in_table("khant",65,3) 

