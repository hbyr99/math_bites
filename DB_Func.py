import pandas as pd
import warnings
from sqlalchemy import create_engine
from sqlalchemy.sql import text


class DB_Func:
    def __init__(self):
        self.connection = create_engine('mysql://root:codio@localhost')
        self.db = None
        self.df = pd.DataFrame()


    def createDB(self, db_name):
        self.db = db_name
        create_db_query = text('CREATE DATABASE IF NOT EXISTS ' + db_name)
        use_database_entry = text("USE " + self.db)
        
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", module = "sqlalchemy")
            self.connection.execute(create_db_query)
            self.connection.execute(use_database_entry)



    def addEntry(self, table, number):
        create_table_query = text("""
        CREATE TABLE IF NOT EXISTS {} (
            number VARCHAR(255) NOT NULL,
            appearances INT UNSIGNED DEFAULT 1,
            UNIQUE KEY (number)
        )
        """.format(table))
        insert_entry = text("""
        INSERT INTO {} (number) 
            VALUES ({})
            ON DUPLICATE KEY UPDATE appearances = appearances + 1 
        """.format(table, number))
        
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", module = "sqlalchemy")
            self.connection.execute(create_table_query)
            self.connection.execute(insert_entry)


    def showTable(self, table):
        show_table_query = 'SELECT * FROM ' + table
        df = pd.read_sql(show_table_query, con=self.connection)
        print(df)
