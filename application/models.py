import flask
from application import db

class vid(db.Document): # original
    episode   =   db.StringField( max_length=10, unique=True )
    title       =   db.StringField( max_length=100 )
    description =   db.StringField( max_length=255 )
    duration     =   db.StringField()
    thumbnail        =   db.StringField( max_length=25 )

# class videos(db.Document): # test
#     episode   =   db.StringField( max_length=10, unique=True )
#     title       =   db.StringField( max_length=100 )
#     description =   db.StringField( max_length=255 )
#     duration     =   db.StringField()
#     thumbnail        =   db.StringField( max_length=25 )