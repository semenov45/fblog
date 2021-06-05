from sqlalchemy import create_engine,Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql+psycopg2://odxxzyohipmskw:e9663c35f76f52bafd96b805f26514be1a7fa19a073ea32ca1e6748ae6d09d91@ec2-54-243-92-68.compute-1.amazonaws.com:5432/d47q8rljmhjuv2')
Session = sessionmaker(bind=engine)
conn = engine.connect()
session= Session()


# # metadata = MetaData()
# # users_table = Table('zhabrcom', metadata,
# #     Column('id', Integer, primary_key=True),
# #     Column('url', String),
# #     Column('title', String),
# #     Column('image', String),
# #     Column('created', String),
# #     Column('author', String),
# #     Column('decript', String)
# # )


# # metadata.create_all(engine)


Base = declarative_base()
class Zhabrcom(Base):
    __tablename__ = 'zhabrcom'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    title = Column(String)
    image = Column(String)
    created = Column(String)
    author = Column(String)
    descrypt = Column(String)
    descrypt_text = Column(String)
    
    def __init__(self, url, title, image,created,author,descrypt,descrypt_text):
        self.url = url
        self.title = title
        self.image = image
        self.created = created
        self.author = author
        self.descrypt = descrypt
        self.descrypt_text = descrypt_text

#     # def __repr__(self):
#     #     return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

# # Создание таблицы
Base.metadata.create_all(engine)
####################################################postresql###################################
# import sqlite3
# def sqlite_conn():

#     con = sqlite3.connect('habr.db')
#     print("connection success")

#     cur = con.cursor()

#     # # Create table
#     # cur.execute('''CREATE TABLE zhabrcom
#     #                (url text, title text, created text, author text,image text,descrypt text)''')
#     cur.execute('''CREATE TABLE IF NOT EXISTS zhabrcom (
#   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
#   url text, 
#   title text, 
#   created text,
#    author text,
#    image text,
#    descrypt text,
#    descrypt_text text);  ''')
#     # # # Insert a row of data
#     # # cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

#     # # # Save (commit) the changes
#    # con.commit()

#     # # We can also close the connection if we are done with it.
#     # # Just be sure any changes have been committed or they will be lost.
#     # con.close()
#     return con

#sqlite_conn()    