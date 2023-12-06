import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

credentials = {
    "DB_PASSWORD": os.getenv("MYSQL_ROOT_PASSWORD"),
    "DB_USER": os.getenv("MYSQL_ROOT_USER"),
}

# create a connection to the mysql database with the connector
mydb = mysql.connector.connect(
    host="localhost",
    user=credentials["DB_USER"],
    password=credentials["DB_PASSWORD"],
    database="test"
)

# create a cursor to execute queries
my_cursor = mydb.cursor()

# select the 'test' database
my_cursor.execute("USE test")

# create a table if it doesn't exist
my_cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")

# add some info
sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
values = ("Jane", 28)
my_cursor.execute(sql, values)
mydb.commit()

# show tables
my_cursor.execute("SHOW TABLES")
for table in my_cursor:
    print(f'Available tables: {table}')

# show info
my_cursor.execute("SELECT * FROM users")
for user in my_cursor:
    print(f'User info: {user}')

# close the connection
my_cursor.close()
mydb.close()

