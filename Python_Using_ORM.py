from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Define database connection and model
engine = create_engine('sqlite:///example.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create table and add data
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

user = User(name='Alice', age=30)
session.add(user)
session.commit()

# Query data
for user in session.query(User):
    print(user.name, user.age)
