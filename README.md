# IDS706 Mini Project5: GroceryDB CRUD Application

## Project Description

This project is a simple Python application that interacts with a SQLite database named `GroceryDB`. It provides basic CRUD functionality: Create, Read, Update, and Delete operations on the `GroceryDB` database. It uses SQLite3 for database interaction and PrettyTable to display the query results in a tabular format.

## Queries Description

### Query 1 - Read Operation
```python
def query1():
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GroceryDB LIMIT 5 OFFSET 1")
    column_names = [description[0] for description in cursor.description]
    table = PrettyTable(column_names)
    for row in cursor.fetchall():
        table.add_row(row)
    print("Top 5 rows of the GroceryDB:")
    print(table)
    conn.close()
    return "Success"
```

