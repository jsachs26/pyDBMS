#Python PostgreSQL Access
# Josh Sachs
# December 2017
# Testing how to access and maniuplate data
#!/usr/bin/python
import psycopg2
import psycopg2.extras

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
    # 12/21/17
    #updated Age to smallInt, and now the ID and the Ages are unique. No longer seeing issue!
    cur.execute("INSERT INTO test(id, name, age, address, salary) VALUES(%(int)s, %(str)s, %(smallint)s, %(char)s, %(real)s);",
                {'int':insertID, 'str':insertName, 'smallint':insertAge, 'char':insertAddress, 'real':insertSalary})

def deleteInputs(conn) :
	cur = conn.cursor()
	print("Let's delete a record! ")
	#deleteOption = raw_input("How do you want to delete a record? ID? Name? Age? Address? Salary? ")    
	deleteYesNo = raw_input("Do you know the ID of the record you want to delete? Yes or No ")

	#Age, Address, and Salary are not unique values, so theoretically someone could delete multiple entries by selecting one of these values. 
	#For a delete operation, we either need to force the user to select from just ID, or ID+Another parameter. 

	if deleteYesNo == "yes": 
		deleteID = raw_input("What's the ID of the record you'd like to delete? ")
		cur.execute("DELETE FROM test WHERE id=(%(int)s);",
                {'int':deleteID})
	elif deleteYesNo == "no":
		print(doQuery(myConnect))
		deleteID = raw_input("Select the ID from the above list: ")
		deleteParameter = raw_input("Select the name, age, address, or salary of the record you'd like to delete? Enter one: ")
		if deleteParameter == "name":
			deleteName = raw_input("Enter the name: ")
			cur.execute("DELETE FROM test WHERE id=(%(int)s) AND name=(%(str)s);",
				{'int':deleteID, 'str':deleteName})
		elif deleteParameter == "age":
			deleteAge = raw_input("Enter the age: ")
			cur.execute("DELETE FROM test WHERE id=(%(int)s) AND age=(%(smallint)s);",
				{'int':deleteID, 'smallint':deleteAge})
		elif deleteParameter =="address":
			deleteAddress = raw_input("Enter the address: ")
			cur.execute("DELETE FROM test WHERE id=(%(int)s) AND address=(%(char)s);",
				{'int':deleteID, 'char':deleteAddress})
		elif deleteParameter == "salary":
			deleteSalary = raw_input("Enter the salary: ")
			cur.execute("DELETE FROM test WHERE id=(%(int)s) AND salary=(%(real)s);",
				{'int':deleteID, 'real':deleteSalary})


def updateQuery(conn):
	
	cur = conn.cursor()
	updateID = raw_input("What's the ID of the record to update? ")
	updateField = raw_input("Update name? age? address? salary? ")

	if updateField == "name":
		updateName = raw_input("Update the name to? ")
		cur.execute("UPDATE test SET Name=(%(str)s) WHERE ID=(%(int)s);",
		{'str':updateName, 'int':updateID})
	elif updateField == "age":
		updateAge = raw_input("Update age to? ")
		cur.execute("UPDATE test SET Age=(%(smallint)s) WHERE ID=(%(int)s);",
		{'smallint':updateAge, 'int':updateID})
	elif updateField == "address":
		updateAddress = raw_input("Where do they live? ")
		cur.execute("UPDATE test SET Address=(%(str)s) WHERE ID=(%(int)s);",
		{'str':updateAddress, 'int':updateID})
	elif updateField == "salary":
		updateSalary = raw_input("How much they make? ")
		cur.execute



def selectQuery (conn):
	cur = conn.cursor()
	cur.execute("SELECT id, name, age, address, salary FROM test" )

	for id, name, age, address, salary in cur.fetchall() :
		print id, name, age, address, salary

#Uses psycopg2 to connect
myConnect = psycopg2.connect(host=hostname, user=username, password=password, database=database)

#Prompt the user to decided what's gonna happen to the Database
queryOp = raw_input("Would you like to delete? insert? list? update? ")

if queryOp == "delete":
	deleteInputs(myConnect)
elif queryOp == "insert":
	insertInputs(myConnect)
elif queryOp == "list":
	selectQuery(myConnect)
elif queryOp == "update":
	updateQuery(myConnect)
else:
	print("please provide a valid input...")


print("-------------------------------------------------")
selectQuery(myConnect)
myConnect.commit()
myConnect.close()
