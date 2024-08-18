import mysql.connector
from mysql.connector import Error

def create_and_verify_database(cursor, database_name):
    """
    Create a database if it does not exist and verify its creation.
    """
    try:
        # Create the database if it does not exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        # Verify if the database was created
        cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
        result = cursor.fetchone()
        for i in result:
            print(i)
        if result:
            print(f"Database '{database_name}' created successfully or already exists.")
        else:
            print(f"Error: Database '{database_name}' was not created.")
    except Error as e:
        print(f"Error occurred: {e}")


def show_all_databases(cursor):
    """
    Retrieve and display all databases in the MySQL server.
    """
    try:
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        print("Databases:")
        for db in databases:
            print(db[0])
    except Error as e:
        print(f"Error occurred: {e}")


def delete_and_verify_database(cursor, database_name):
    """
    Delete a database if it exists and verify its deletion.
    """
    try:
        # Drop the database if it exists
        cursor.execute(f"DROP DATABASE IF EXISTS {database_name}")
        print(f"Attempted to drop database '{database_name}'")
        # Verify if the database was deleted
        cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
        result = cursor.fetchone()
        if not result:
            print(f"Database '{database_name}' deleted successfully.")
        else:
            print(f"Error: Database '{database_name}' was not deleted.")
    except Error as e:
        print(f"Error occurred: {e}")


from mysql.connector import Error

def use_and_verify_database(cursor, database_name):
    """
    Select a database for use and verify that it is set as the current database.
    """
    try:
        # Select the database
        cursor.execute(f"USE {database_name}")
        print(f"Attempted to use database '{database_name}'")
        # Verify if the database is set as the current database
        cursor.execute("SELECT DATABASE()")
        result = cursor.fetchone()
        if result and result[0] == database_name:
            print(f"Database '{database_name}' is now in use.")
        else:
            print(f"Error: Database '{database_name}' is not in use.")
    except Error as e:
        print(f"Error occurred: {e}")
