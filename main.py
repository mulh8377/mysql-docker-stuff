from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


engine = create_engine('mysql://example:example@172.18.0.2/test')

# Create a connection to the database


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __repr__(self) -> str:
        return f'User(id={self.id}, name={self.name})'

Base.metadata.create_all(engine)

def create_user(session: Session, user: User):
    session = Session(engine)
    user = User(name=name)
    session.add(user)
    session.commit()

session = Session(engine)

_user = User(name='test')
print(_user)
session.add(_user)
session.commit()

def fetch_user(session: Session):
    session = Session(engine)
    return session.query(User).all()

print(fetch_user(session))
