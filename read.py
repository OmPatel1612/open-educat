from sqlalchemy.orm import sessionmaker
from main import User, engine
Session= sessionmaker(bind=engine)
session=Session()
user=session.query(User).all()
for u in user:
    print(f"id:{u.id},NAme:{u.Name},Marks:{u.Marks}")