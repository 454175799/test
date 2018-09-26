from sqlalchemy import Column,INTEGER,String,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine("mysql+pymysql://root:123456@172.17.0.2:3306/ceshi",echo=True)


class user(Base):
    __tablename__ = 'user'
    id = Column(INTEGER,primary_key=True,autoincrement=True)
    name = Column(String(32),nullable=True)
    address = Column(String(32))

#Base.metadata.create_all(engine)

DBsession =sessionmaker(engine)

session = DBsession()

new_user = user(name='qaq',address="zhejiang")

session.add_all([new_user])

session.commit()

session.close()
