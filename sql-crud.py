from sqlalchemy import (
    create_engine,  Integer, String,  Column
)
# we don't need to import Table because we will use python classes -> collection of methods to perform certain purpose.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# connect to database 
db = create_engine("postgresql:///chinook")

# get metadata produced from out db which holds the schema of every table
base = declarative_base()


# create the class which is nothing but a table to be added to the database
class Programmer(base):
    __tablename__ ="Programmer"
    Id=Column("Id", Integer, primary_key=True)
    first_name=Column("First_name", String)
    last_name=Column("Last_name", String)
    gender=Column("Gender", String)
    nationality=Column("Nationality", String)
    famous_for=Column("Famous_for", String)


# instead of connecting directly to the DB, we will ask for a session 
# creating a session which we can direct to the database engine (DB

Session = sessionmaker(db)
session = Session() # use highest level of abstraction

# create database from declarative_base sub-class 
base.metadata.create_all(db)

# create instance of the programmer class
ada_lovelace=Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="Female",
    nationality="British",
    famous_for="Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

mazen_al_ali = Programmer(
    first_name="Mazen",
    last_name="Al Ali",
    gender="M",
    nationality="German/Syrian",
    famous_for="C++/Qt - Full-Stack"
)


# use the session to add the instance 
# session.add(ada_lovelace)
#session.add(grace_hopper)
#session.add(alan_turing)
#session.add(margaret_hamilton)
#session.add(bill_gates)
#session.add(tim_berners_lee)
#session.add(mazen_al_ali)

# updating single record
# programmer =session.query(Programmer).filter_by(Id=10).first()
# programmer.famous_for=" Front & Backend Developer"

# commit the session which holds the instance of the class (table)
# session.commit()


# updating multiple records
people = session.query(Programmer)
for person in people:
    if person.gender=="F":
        person.gender="Female"
    elif person.gender=="M":
        person.gender="Male"
    
    session.commit()



# deleting a record should be done very carefully and defensive programming is recommended to confirm deletion process
f_name=input("Enter first name: ")
l_name=input("Enter last name: ")
# using first is import to get the first exact match
person_to_delete=session.query(Programmer).filter_by(first_name=f_name, last_name=l_name).first()

if person_to_delete is not None:
    print("Programmer found : ", person_to_delete.first_name+" "+person_to_delete.last_name)
    confirmation=input("Are you sure you want to delete the person? (y/n)")
    if confirmation.lower()=="y":
        session.delete(person_to_delete)
        print("Person has been deleted")
    else:
        print("Person wasn't deleted !")
else:
    print("No records found")



# WARNING FOLLOWING SYNTAX ARE ONLY FOR DEMONSTRATING PURPOSES ON HOW TO DELETE ENTIRE RECORDS
all_programmers=session.query(Programmer)
for single_prog in all_programmers:
    session.delete(single_prog)
    session.commit()



# check if the instance is added
programmers=session.query(Programmer)

for programmer in programmers:
    print(
        programmer.Id,
        programmer.first_name+" "+programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )