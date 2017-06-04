from peewee import *
import datetime

db = SqliteDatabase('posts.db')

class Post(Model):
      username = CharField()
      caption = CharField()
      file = CharField()
	  date = DateTimeField(default = datetime.datetime.now)
     
   class Meta:
           database = db

def initialize_db():
    db.connect()
    db.create_tables([Post], safe=True)	