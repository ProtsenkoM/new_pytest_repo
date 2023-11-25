import sqlite3
from utilities.deco import singleton


@singleton
class BaseDBConnector:
    def __init__(self, db_params):
        self.__path = db_params
        self.conn = sqlite3.connect(database=self.__path)
        self.cursor = self.conn.cursor()

