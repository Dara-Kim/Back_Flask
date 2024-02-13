from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import model
import databaseConfig

# mysql database 연결 #
engine = create_engine(databaseConfig.getURI(),encoding='utf-8')
model.init_db(engine)

# mysql database와 데이터를 주고받을 통신 연결 #
Session = sessionmaker(engine)
session = Session()
session.commit()
print("-----session commit complete -----")

# Database에서 데이터 통신 #

#example
profile1=session.query(model.PROFILE).first()
print(profile1.ID)