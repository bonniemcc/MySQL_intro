''' Using MySQL with Python '''


# First import MySQL and Pandas libraries
# Separately import Error function for easy access

import mysql.connector
from mysql.connector import Error
import pandas as pd
from getpass import getpass



#####################################################################
######################### DEFINE FUNCTIONS ##########################
#####################################################################


''' Function to establish connection to the MySQL Community Server:
        Arguments:
            host_name (str)
            user_name (str)
            user_password (str)
        Returns:
            connection object

'''

def create_server_connection(host_name, user_name, user_password):
    # Close any exsisting connections
    connection = None 
    # Try to create a connection using the user specified arguments
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        # If successful print:
        print("MySQL Database connection successful")
    # If unsuccessful print the error returned by the server
    except Error as err:
        print(f"Error: '{err}'")

    return connection

#####################################################################

''' Function to create a new database: 
        Arguments:
            connection (connection object)
            query (SQL query string)

'''

def create_database(connection, query):
    # Use cursor method on connection object to create a cursor object
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

#####################################################################

''' Function to connect to specific database:
    (same as 'create_server_connection" function but 
        with extra argument 'db_name' (str))

'''

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

#####################################################################

''' Function to execute a query:
    (same as 'create_database' function but with added line of code)    

'''

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        # Use commit method to ensure queries are implemented
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

#####################################################################
#####################################################################


def main():

    # Prompt user for server password
    #pswd = input("Please enter the password to connect to MySQL Server: ")
    pswd = getpass()
    # Create connection object 
    connection = create_server_connection("localhost", "root", pswd)
    # Create database
    #create_database_query = "CREATE DATABASE school"
    #create_database(connection, create_database_query)

main()