from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///coco.db', echo=True , connect_args={'check_same_thread': False}) #, timeout=10, uri=True , check_same_thread=True
Base = declarative_base()

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer,primary_key=True)
    long = Column(String(10))
    subject = Column(String(50))
    comment = Column(String(50))
    created_at = Column(DateTime)
    created_by = Column(String(50))
    
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    dname = Column(String)
    roll = Column(String)
    
Session = sessionmaker(bind=engine)
SESSION = Session()
Base.metadata.create_all(engine)
userdata = User(
    name = "kouki",
    password = "admin",
    dname = "管理者",
    roll = True
)
SESSION.add(userdata)
SESSION.commit()