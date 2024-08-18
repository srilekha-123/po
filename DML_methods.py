from mysql.connector import Error
def insert_and_verify_data(cursor, conn, table_name, insert_query, data):
    """
    Insert data into the specified table and verify the insertion.
    """
    try:
        cursor.executemany(insert_query, data)
        conn.commit()
        print(f"Data inserted into '{table_name}' successfully.")
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        row_count = cursor.fetchone()[0]
        print(f"Total number of rows in '{table_name}': {row_count}")
    except Error as e:
        print(f"Error occurred: {e}")



def update_data(cursor, conn, table_name, set_clause, condition):
    """
    Updates data in the specified table and verifies the update.
    """
    query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
    try:
        cursor.execute(query)
        conn.commit()
        affected_rows = cursor.rowcount
        if affected_rows > 0:
            print(f"Data updated in '{table_name}' successfully.")
        else:
            print(f"No rows were updated in '{table_name}'.")
    except Error as e:
        print(f"Error occurred: {e}")


def delete_data(cursor, conn, table_name, condition):
    """
    Deletes data from the specified table based on the condition and verifies the deletion.
    """
    query = f"DELETE FROM {table_name} WHERE {condition}"
    try:
        cursor.execute(query)
        conn.commit()
        affected_rows = cursor.rowcount
        if affected_rows > 0:
            print(f"Data deleted from '{table_name}' successfully.")
        else:
            print(f"No rows were deleted from '{table_name}'.")
    except Error as e:
        print(f"Error occurred: {e}")


def select_data(cursor, table_name, columns, condition=None):
    """
    Selects and retrieves data from the specified table.
    """
    query = f"SELECT {columns} FROM {table_name}"
    if condition:
        query += f" WHERE {condition}"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            print(f"Data retrieved from '{table_name}':")
            for row in results:
                print(row)
        else:
            print(f"No data found in '{table_name}' with the given condition.")
    except Error as err:
        print(f"Error: {err}")


def execute_query(cursor, conn, query, data=None):
    """
    Executes a given SQL query with optional data.
    """
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
            results=cursor.fetchall()
            for row in results:
                print(row)
        if query.strip().upper().startswith(('INSERT', 'UPDATE', 'DELETE')):
            cursor.connection.commit()
        print("Query executed successfully.")
    except Error as err:
        print(f"Error: {err}")