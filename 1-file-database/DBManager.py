import sqlite3

database = "PATH/TO/DATABASE.db" # Note doesn't have to be complete path, It can also be just FOLDER_CONTAINING_DATABSE/database.db
# If there is no such folder then just type database.db

def createTables():
  db = sqlite3.connect(database)
  
  # To generate table creation statements you can use https://editor.datatables.net/generator/ | Its a very useful website, I'm using it from time to time
  # I suggest using 'IF NOT EXISTS' statement that will create sayed table if it doens't exist in sayed file.
  
  
  sql_statement = '''CREATE TABLE IF NOT EXISTS `TABLENAME` (
	  `id` int(10) NOT NULL,
	  PRIMARY KEY( `id` )
  );'''
  
  cursor = db.cursor() # Creates a "Cursor" to read & write data if required
  
  cursor.execute(sql_statement) # Executes our sql statement to create a table
  
  db.commit() # Commits changes made to the sql database It basically "saves" the data we gave it.
  
  print("Created Tables Successfuly") # To verify our function is finished execution and the table is created and saved
  
def change(table,user,value,newValue):
  db = sqlite3.connect(database) # Connects to database
  
  # user needs to be the id of said user (e.g: 59654301232)
  
  # value should be the name of the value (e.g: 'cash')
  
  # newValue should be the value you want to be set (e.g: 25) NOTE: It depends on what type of data you use in the table
  # for the value, If its varchar(255) give it a string, if its int(9-999) or numeric(9,2) give it numbers
  
  # table should be the name of the table
  