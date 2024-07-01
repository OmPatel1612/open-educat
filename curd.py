from sqlalchemy.orm import sessionmaker
from main import User, engine
Session= sessionmaker(bind=engine)
session=Session()
user=User(Name='''om''',Marks="90")
user_2=User(Name='''sumit''',Marks="95")
user_3=User(Name='''mehul''',Marks="60")
user_4=User(Name='''sachin''',Marks="50")
user_5=User(Name='''pujan''',Marks="88")
session.add_all([user_2,user_3,user_4,user_5])
session.commit()
