import pandas as pd
from mysql.connector import connect, Error

class DB_Func:
    def __init__(self, host, user):
        self.host = host
        self.user = user
        self.connection = connect(
            host=self.host,
            user=self.user,
            password = 'Password',
        )
        self.db = None
        self.df = pd.DataFrame()


    def createDB(self, db_name):
        try:
            self.db = db_name
            create_db_query = 'CREATE DATABASE IF NOT EXISTS ' + db_name + '; '
            use_database_entry = "USE " + self.db
            
            with self.connection.cursor() as cursor:
                cursor.execute(create_db_query)
                cursor.execute(use_database_entry)
                self.connection.commit()
                
        except Error as e:
            print(e)

    def addEntry(self, table, number):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS {} (
            number VARCHAR(255) NOT NULL,
            appearances INT UNSIGNED DEFAULT 1,
            UNIQUE KEY (number)
        )
        """.format(table)
        insert_entry = """
        INSERT INTO {} (number) 
            VALUES ({})
            ON DUPLICATE KEY UPDATE appearances = appearances + 1 
        """.format(table, number)

        with self.connection.cursor() as cursor:
            cursor.execute(create_table_query)
            cursor.execute(insert_entry)
            self.connection.commit()


    def showTable(self, table):
        show_table_query = 'SELECT * FROM ' + table
        df = pd.read_sql(show_table_query, con=self.connection)
        print(df)