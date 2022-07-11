from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///users.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base): 
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self): 
        return f'<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})'


if __name__ == '__main__': 
    Base.metadata.create_all(engine)

    # madeline_user = User(name='Madeline', fullname='Madeline Caples', nickname='Maddie')
    # print(madeline_user.name)
    # print(madeline_user.id)
    # session.add(madeline_user)
    # session.commit()
    # print(madeline_user.id)

    # new_users = [
    #     User(name='Alejandro', fullname='Alejandro Piad', nickname='Ale'),
    #     User(name='Christina', fullname='Christina Jones', nickname='Christy')
    # ]

    # session.add_all(new_users)
    # session.commit()

    # for user in new_users: 
    #     print(user.id)