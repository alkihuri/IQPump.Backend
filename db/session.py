# Подключение к БД

## sql lite 


import sqlite3


class Session:

    PATH = "app/db/test.db"    

    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.PATH)
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.connection.commit()
            self.connection.close()
            self.cursor.close() 
            return True
        except Exception as e:
            print(e)
            return False