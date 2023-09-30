"""Query the database"""

import sqlite3

from prettytable import PrettyTable

def query1():
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GroceryDB LIMIT 5 OFFSET 1") # Skipping the first row (header)
    
    # Fetching column names
    column_names = [description[0] for description in cursor.description]
    
    table = PrettyTable(column_names)  # Initializing table with column names

    # Fetching rows and adding them to the table
    for row in cursor.fetchall():
        table.add_row(row)
    
    print("Top 5 rows of the GroceryDB:")
    print(table)  # Printing table
    
    conn.close()
    return "Success"

def query2():
    '''Update the count_products of the arabica coffee in the GroceryDB table'''
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()

    # Define the new count_products value
    new_count_products = 100
    item_name = "arabica coffee"

    cursor.execute("UPDATE GroceryDB SET count_products = ? WHERE general_name = ?", (new_count_products, item_name))
    conn.commit()
    conn.close()
    # Print the updated row
    print("Updated row:")
    query1()
    return "Success"
