from sqlalchemy import Column,String,INTEGER,Table,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base("mysql+pymysql://root:123456@172.16.0.40:3306/ceshi")
engine = create_engine()

jumpuser_m2m_jumpgroup = Table('jumpuser_m2m_jumpgroup',Base.metadata,
                               Column('jumpuser_id',INTEGER,ForeignKey('jump_user.id')),
                                Column('jumpgroup_id',INTEGER,ForeignKey('jump_group_id'))
                               )

class JumpUser(Base):
    __tablename__ = "jump_user"
    id = Column(INTEGER,primary_key=True,autoincrement=True)
    username = Column(String(32),nullable=True)
    password = Column(String(32),nullable=True)

    def __repr__(self):
        return "<jump_user>  username:%s" %(self.username)


class JumpGroup(Base):
    __tablename__ = "jump_group"
    id = Column(INTEGER,primary_key=True,autoincrement=True)
    group_name = Column(String(32))
    jump_user = relationship('jump_user',secondary=jumpuser_m2m_jumpgroup,backref='jump_group')

    def __repr__(self):
        return "<jump_group> group_name:%s" %(self.group_name)

class RemoteUser(Base):
    __tablename__ = "remote_user"
    id = Column(INTEGER,primary_key=True,autoincrement=True)
    username = Column(String(16),nullable=True)
    password = Column(String(32))
    public_key = Column(String(32))

    def __repr__(self):
        return "<remote_user> username:%s" %(self.username)


class RemoteHost(Base):
    __tablename__ = "remote_host"
    id = Column(INTEGER,primary_key=True,autoincrement=True)
    ip = Column(String(32),nullable=True)
    port = Column(INTEGER,default=22)

    def __repr__(self):
        return "<remote_host> ip:%s,port:%s" %(self.ip,self.port)


