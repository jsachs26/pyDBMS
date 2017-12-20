#Python PostgreSQL Access
# Josh Sachs
# December 2017
# Testing how to access and maniuplate data
#!/usr/bin/python
import psycopg2

#port can be declared but defaults to 5432 if not provided. 
hostname = 'localhost'
username = 'postgres'
password = 'root'
database = 'testDB'

def insertInputs(conn) :
    cur = conn.cursor()
    print("Insert a new record! ")
    insertID = raw_input("What's the ID of the new record? ")
    insertName = raw_input("What's the name of the new record? ")
    insertAge = raw_input("How old are they? ")
    insertAddress = raw_input("Where they live? ")
    insertSalary = raw_input("How much they make? ")

    #Data from raw_input has to be formatted in this manner to be inserted in to the SQL commands. 
    #This input seems to be inserting the Age input as the ID as well. Whatever the age is assigned to, is also the ID. 
    #This might be because of the data type, which could cause issues with the real OMPS database, need to investigate. 
    cur.execute("INSERT INTO test(id, name, age, address, salary) VALUES(%(int)s, %(str)s, %(int)s, %(char)s, %(real)s);",
                {'int':insertID, 'str':insertName, 'int':insertAge, 'char':insertAddress, 'real':insertSalary})

def deleteInputs(conn) :
	cur = conn.cursor()
	print("Let's delete a record! ")
	deleteOption = raw_input("How do you want to delete a record? ID? Name? Age? Address? Salary? ")    

	if deleteOption == "ID":
		deleteID = raw_input("What's the ID of the record you'd like to delete? ")
		cur.execute("DELETE FROM test WHERE id=(%(int)s);",
                {'int':deleteID})
	elif deleteOption == "name":
		deleteName = raw_input("What's the name of the record you'd like to delete? ")
		cur.execute("DELETE FROM test WHERE name=(%(str)s);",
                {'str':deleteName})
	elif deleteOption == "age":
		deleteAge = raw_input("What's the age of the record(s) you'd like to delete? ")
		cur.execute("DELETE FROM test WHERE age=(%(int)s);",
                {'int':deleteAge})
	elif deleteOption == "address":
		deleteAddress = raw_input("What's the address of the record(s) you'd like to delete? ")
		cur.execute("DELETE FROM test WHERE address=(%(char)s);",
                {'char':deleteAddress})
	elif deleteOption == "salary":
		deleteSalary = raw_input("What's the salary of the record(s) you'd like to delete? ")
		cur.execute("DELETE FROM test WHERE salary=(%(real)s);",
                {'real':deleteSalary})
	else:
		print("You didn't enter a valid option...")

def doQuery (conn) :
	cur = conn.cursor()
	cur.execute("SELECT id, name, age, address, salary FROM test" )

	for id, name, age, address, salary in cur.fetchall() :
		print id, name, age, address, salary

#Uses psycopg2 to connect
myConnect = psycopg2.connect(host=hostname, user=username, password=password, database=database)

#Prompt the user to decided what's gonna happen to the Database
queryOp = raw_input("Would you like to delete? insert? list? ")

if queryOp == "delete":
	deleteInputs(myConnect)
elif queryOp == "insert":
	insertInputs(myConnect)
elif queryOp == "list":
	doQuery(myConnect)
else:
	print("please provide a valid input...")


print("-------------------------------------------------")
doQuery(myConnect)
myConnect.commit()
myConnect.close()
