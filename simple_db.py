import sqlite3


def create_database():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    # create a table
    cursor.execute("""CREATE TABLE employees
                          (name text, position text, arrival_date text,
                           service text, salary text)
                       """)
    # insert some data
    cursor.execute("INSERT INTO employees VALUES "
                   "('Dupont', 'engineer', '7/24/2012',"
                   "'DSI', '2000')")

    # save data to database
    conn.commit()

    # insert multiple records using the more secure "?" method
    employees = [('Deghdegh', 'HR', '7/9/2002',
               'HR', '3000'),
              ('Dridi', 'CISO', '2/1/2011',
               'DSI', '100'),
              ('Zhu', 'HR',
               '4/17/2012', 'HR', '2000'),
              ('Firpion', 'DSI', '4/10/2012',
               'engineer', '3000')]
    cursor.executemany("INSERT INTO employees VALUES (?,?,?,?,?)",
                       employees)
    conn.commit()


def delete_position(position):
    """
    Delete an position from the database
    """
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    sql = """
    DELETE FROM employees
    WHERE position = ?
    """
    cursor.execute(sql, [(position)])
    conn.commit()
    cursor.close()
    conn.close()


def update_position(position, new_position):
    """
    Update the position name
    """
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    sql = """
    UPDATE employees
    SET position = ?
    WHERE position = ?
    """
    cursor.execute(sql, (new_position, position))
    conn.commit()
    cursor.close()
    conn.close()


def select_all_employees(position):
    """
    Query the database for all the employees by a particular position
    """
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    sql = "SELECT * FROM employees WHERE position=?"
    cursor.execute(sql, [(position)])
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


if __name__ == '__main__':
    import os

    if not os.path.exists("employees.db"):
        create_database()

    delete_position('HR')
    update_position('HR', 'DIRECTOR')
    print(select_all_employees('CEO'))