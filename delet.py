from sqlalchemy.orm import sessionmaker
from main import User, engine
Session= sessionmaker(bind=engine)
session=Session()
user=session.query(User).filter_by(id=1).one_or_none()
session.delete(user)
session.commit()