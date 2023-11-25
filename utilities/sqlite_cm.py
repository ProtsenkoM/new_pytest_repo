import sqlite3
from utilities.deco import singleton


@singleton
class Sqlite:
    def __init__(self, db_params):
        self.path = db_params

    def __enter__(self):
        self.conn = sqlite3.connect(database=self.path)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
