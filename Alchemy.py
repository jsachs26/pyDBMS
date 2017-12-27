from sqlalchemy import create_engine  
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

db_string = "postgres://postgres:root@localhost/testDB"

db = create_engine(db_string)  
base = declarative_base()

class Film(base):  
    __tablename__ = 'films'

    title = Column(String, primary_key=True)
    director = Column(String)
    year = Column(String)

Session = sessionmaker(db)  
session = Session()

base.metadata.create_all(db)

# Create 
#blade_runner = Film(title="Blade Runner 2049", director="Dennis Villeneuve", year="2017")
#lady_bird = Film(title="Lady Bird", director="Greta Gerwig", year="2017")
#session.add(doctor_strange)
#session.add(blade_runner)
#session.add(lady_bird)
#session.commit()

print("Insert a movie? ")
insert = raw_input("want to insert a movie? ")

if insert == "yes":
	insertTitle = raw_input("What's the name of the movie? ")
	insertDirector = raw_input("Who's the director? ")
	insertYear = raw_input("What year was this released? ")
	insertMovie = Film(title=insertTitle, director=insertDirector, year=insertYear)
	session.add(insertMovie)
	session.commit()
else:
	print("I guess we have nothing to insert... ")

print("Delete a movie? ")
delete = raw_input("Want to delete a movie? ")

if delete == "yes":
	deleteOption = raw_input("Do you know the title of the movie?(Y/N) ")
	if deleteOption == "yes":
		deleteTitle = raw_input("What's the title of the film you'd like to delete? ")
		deleteTitleStatement= session.query(Film).filter_by(title=deleteTitle).one()
		session.delete(deleteTitleStatement)
		session.commit()
	else:
		deleteChoice = raw_input("Do you know the director or year of release? (director/year) ")
		if deleteChoice == "director":
			deleteDirector = raw_input("What's the name of the director who's films you'd like to delete? ")
			deleteDirectorStatement = session.query(Film).filter_by(director=deleteDirector).one()
			session.delete(deleteDirectorStatement)
			session.commit()
		elif deleteChoice == "year":
			deleteYear = raw_input("What year was the film released that you'd like to delete? ")
			deleteYearStatement = session.query(Film).filter_by(year=deleteYear).one()
			session.delete(deleteYearStatement)
			session.commit()


print("Update a record?")
updateTitle = raw_input("What is the title of the film you'd like to update? ")
updateWhat = raw_input("Do you wanna update the title, director, or year? ")
if updateWhat == "title":
	newTitle = raw_input("What should the title be? ")
	updateTitle = session.query(Film).filter_by(title=updateTitle).one()
	updateTitle.title = newTitle
	session.commit()
elif updateWhat == "director":
	newDirector = raw_input("Who should the director be? ")
	updateDirector = session.query(Film).filter_by(title=updateTitle).one()
	updateDirector.director = newDirector
	session.commit()
elif updateWhat == "year":
	newYear = raw_input("What should the year be? ")
	updateYear = session.query(Film).filter_by(title=updateTitle).one()
	updateYear.year = newYear
	session.commit()
else:
	print("Bad input!")
# Displays all entries in the table, films. 
films = session.query(Film)  
for film in films:  
    print(film.title, film.director, film.year)

