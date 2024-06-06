from sqlalchemy import (
    create_engine, Float, Integer, String, ForeignKey, Column
)
# we don't need to import Table because we will use python classes -> collection of methods to perform certain purpose.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# connect to database 
db = create_engine("postgresql:///chinook")

# get metadata produced from out db which holds the schema of every table
base = declarative_base()


# create the tables Artist, Album and Track and inherit the base 
class Artist(base):
    __tablename__="Artist"
    ArtistId=Column(Integer, primary_key=True)
    Name=Column(String)

class Album(base):
    __tablename__="Album"
    AlbumId=Column(Integer, primary_key=True)
    Title=Column(String)
    ArtistId=Column(Integer,ForeignKey("Artist.ArtistId"))

# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)
 


# instead of connecting directly to the DB, we will ask for a session 
# creating a session which we can direct to the database engine (DB

Session = sessionmaker(db)
session = Session() # use highest level of abstraction

# create database from declarative_base sub-class 
base.metadata.create_all(db)

# queries 
# query 1 - select everything in the artist table
print("Query 1 selecting everything from Artist table")
artists = session.query(Artist)
for artist in artists:
    print(artist.ArtistId, artist.Name, sep=" | ")

print("#######################################")
print("     Query 2 only the name")
for artist in artists:
    print( artist.Name)

# Query 3 print artist where name = Queen 
print("Query 3 to slect values of Name = Queen from Artist table")
artist = session.query(Artist).filter_by(Name="Queen").first()
print(artist.ArtistId, artist.Name, sep=" | ")
print (" ####### END OF QUERY #######################")



print("#######################################")
print("Query 4 : select only by 'ArtistId' = 51 from Artist table")
artist = session.query(Artist).filter_by(ArtistId=51).first()
print(artist.ArtistId, artist.Name, sep=" | ")
print (" ####### END OF QUERY #######################")

print("#######################################")
print("Query 5 : select only by Albums with Artist ID = 51 from Album table")
albums = session.query(Album).filter_by(ArtistId=51)
for album in albums:
    print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")
print (" ####### END OF QUERY #######################")

print("#######################################")
print("Query 6 : select only by Track  where composer is Queen table")
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print( track.TrackId, track.Name, track.AlbumId, track.MediaTypeId, track.GenreId, track.Composer, track.Milliseconds, track.Bytes, track.UnitPrice, sep=" | ")
print (" ####### END OF QUERY #######################")