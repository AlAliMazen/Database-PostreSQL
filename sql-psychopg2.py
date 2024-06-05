import psycopg2

# connect to "chinnok" database, you can also specify other parameters such as host, username and password
connection = psycopg2.connect(database="chinook")




# build a cursor object of the database -> cursor is just like a set in JS or List in python 
# anything we get from the query will become part of the cursor.
# we use a for loop to iterate over a cursor
cursor = connection.cursor()

# Queries  query-1 select all records from artist - >must use single quotes 
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 getting only the name column from artist table
cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 getting the artist of with Queen name -> we need to use String %s , as second argument we use the brackets inside which we can either use the double or single quotes
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s ',['Queen'])


# Query 4 same as previous result but the place holder %s will be a number
#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s ',[51])

# Query 5 same as previous result but the place holder %s will be a number
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s ',[51])


# Query 6 same but from Track where composer = Queen
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s ',["Queen"])

# when we need to fetch all records(multiple), then we use fetchall method, other wise we use fetchONe for single records
results = cursor.fetchall()

# for single records we use fetchOne
# results = cursor.fetchone()

# we need to end the connection when result is et 
connection.close()


# iterate over the result
for result in results:
    print(result)