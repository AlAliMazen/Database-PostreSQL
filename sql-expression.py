from sqlalchemy import(
    create_engine, Float, String, Integer, MetaData, Table, Column,ForeignKey
)

# link python to our chinook database, 
db = create_engine("postgresql:///chinook")


# metaData which is data about the schema of each table 
meta=MetaData(db)
# create the schema of each table 
# artist table schema SELECT * FROM "Artist" WHERE false;
artist_tbl=Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

album_tbl=Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_tbl.ArtistId"))
)

track_tbl=Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_tbl.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)


)

# create the connection
with db.connect() as connection:
    # build a select expression to use every time
    #query 1 select everything from artist table
    #select_query=artist_tbl.select()

    # query 2 select only name from the artist table
    #select_query=artist_tbl.select().with_only_columns([artist_tbl.c.Name])

    # query 3 select only queen as name from artist table
    select_query =artist_tbl.select().where(artist_tbl.c.Name=="Queen")

    # query 4 select only queen id as 51 as name from artist table
    select_query =artist_tbl.select().where(artist_tbl.c.ArtistId==51)

    # query 5 select only the albums where queen is the artist id = 51
    select_query=album_tbl.select().where(album_tbl.c.ArtistId==51)
    # query 6 select all tracts where composer is queen from tract table

    select_query=track_tbl.select().where(track_tbl.c.Composer=="Queen")

    # execute the selection and save it in a variable
    results=connection.execute(select_query)
    for result in results:
        print(result)