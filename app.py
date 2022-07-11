# import models file 
from models import Base, session, Book, engine
# main menu - add, search, analysis, exit, view
# add books to db
# edit books
# delete books from db
# search function 
# data cleaning functions
# loop runs program until user exits


if __name__ == '__main__': 
    Base.metadata.create_all(engine)