import sqlite3
from sqlite3 import Error


SQL_PATH = "./data/dictionary.db"


class SqlInterface:
    def __init__(self):
        self.connection = None
        try:
            self.connection = sqlite3.connect(SQL_PATH)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
