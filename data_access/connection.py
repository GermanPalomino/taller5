import pyodbc

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._connection = None
        return cls._instance

    def connect(self, driver, server, database):
        if self._connection is None:
            self._connection = pyodbc.connect(
                f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
            )

    def get_connection(self):
        return self._connection

    def close_connection(self):
        if self._connection:
            self._connection.close()
            self._connection = None