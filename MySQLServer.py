import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@25050Eight"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Close cursor and connection
        try:
            if cursor:
                cursor.close()
            if connection.is_connected():
                connection.close()
        except NameError:
            pass

if __name__ == "__main__":
    create_database()
