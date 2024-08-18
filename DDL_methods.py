from mysql.connector import Error
def create_and_verify_table(cursor, table_name, table_creation_query):
    """
    Create a table if it does not exist and verify its creation.
    """
    try:
        cursor.execute(table_creation_query)
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        result = cursor.fetchone()
        if result:
            print("successfully created the table")
    except Error as e:
        print(f"Error occurred: {e}")


def show_all_tables(cursor):
    """
    Retrieve and print all tables in the current database.
    """
    try:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        if tables:
            print("Tables in the current database:")
            for table in tables:
                print(table[0])
        else:
            print("No tables found in the current database.")
    except Error as e:
        print(f"Error occurred: {e}")


def describe_table(cursor, table_name):
    """
    Retrieve and print the structure of the specified table.
    """
    try:
        cursor.execute(f"DESCRIBE {table_name}")
        columns = cursor.fetchall()
        if columns:
            print(f"Structure of table '{table_name}':")
            for column in columns:
                print(column)
        else:
            print(f"No structure found for table '{table_name}'.")
    except Error as e:
        print(f"Error occurred: {e}")


def alter_table(cursor, table_name, alter_query):
    """
    Alter the specified table based on the provided SQL query and verify the change.
    """
    try:
        cursor.execute(alter_query)
        print(f"Alteration query executed on table '{table_name}': {alter_query}")
        cursor.execute(f"DESCRIBE {table_name}")
        columns = cursor.fetchall()
        print(f"Structure of table '{table_name}' after alteration:")
        for column in columns:
            print(column)
    except Error as e:
        print(f"Error occurred while altering the table '{table_name}': {e}")

def truncate_table(cursor, table_name):
    """
    Truncate the specified table and verify if it has been emptied.
    """
    try:
        cursor.execute(f"TRUNCATE TABLE {table_name}")
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        result = cursor.fetchone()
        if result and result[0] == 0:
            print(f"Table '{table_name}' truncated successfully and is now empty.")
        else:
            print(f"Error: Table '{table_name}' was not truncated successfully.")
    except Error as e:
        print(f"Error occurred while truncating the table '{table_name}': {e}")
        

def drop_table(cursor, table_name):
    """
    Drop the specified table if it exists and verify its deletion.
    """
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        result = cursor.fetchone()
        if not result:
            print(f"Table '{table_name}' dropped successfully.")
        else:
            print(f"Error: Table '{table_name}' was not dropped.")
    except Error as e:
        print(f"Error occurred while dropping the table '{table_name}': {e}")
