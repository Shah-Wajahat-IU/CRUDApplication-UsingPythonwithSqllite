import sqlite3
from sqlite3 import Error

def createConnection(db_file):
    conn=None
    try:
        conn=sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
if __name__=='__main__':
    createConnection(r"C:\Users\shahw\PycharmProjects\CurdAppliationPython\app.db")