#!/usr/bin/env python3
"""
This script connects to the MySQL server and
creates a database named alx_book_store if it does not exist.
"""

import mysql.connector
from mysql.connector import Error

try:
    # Connect to the MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='your_username',      # <-- Replace with your MySQL username
        password='your_password'   # <-- Replace with your MySQL password
    )
    if connection.is_connected():
        cursor = connection.cursor()
        # Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
