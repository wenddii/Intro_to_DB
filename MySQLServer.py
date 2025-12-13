#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error


def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@25050Eight"
        )

        if connection.is_connected():
            return connection

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    return None


def create_database(database_name):
    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS {database_name}"
        )
        print(f"Database '{database_name}' created successfully!")

    except Error as e:
        print(f"Error creating database: {e}")

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    create_database("alx_book_store")
