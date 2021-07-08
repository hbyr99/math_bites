import pandas as pd
import plotly.graph_objects as go
import warnings
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.exc import ProgrammingError


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
            entry INT NOT NULL,
            appearances INT UNSIGNED DEFAULT 1,
            UNIQUE KEY (entry)
        )
        """.format(table))
        insert_entry = text("""
        INSERT INTO {} (entry) 
            VALUES ('{}')
            ON DUPLICATE KEY UPDATE appearances = appearances + 1 
        """.format(table, number))
        
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", module = "sqlalchemy")
            self.connection.execute(create_table_query)
            self.connection.execute(insert_entry)


    def showTable(self, table):
        show_table_query = 'SELECT * FROM ' + table
        try:
            df = pd.read_sql(show_table_query, con=self.connection)
            print(df)
        except ProgrammingError as e:
            print("No search history found! ")


    def showScatter(self, table):
        fetch_table_query = 'SELECT * FROM ' + table
        try:
            df = pd.read_sql(fetch_table_query, con=self.connection)
        except ProgrammingError as e:
            print("No search history found! ")
            return

        fig = go.Figure(data = go.Scatter(x = df['entry'],
                                          y = df['appearances'],
                                          mode = 'markers',
                                          marker_color = df['appearances'],
                                          text = df['entry']))
        fig.update_layout(title = table.capitalize())
        fig.write_html(table + '.html')
        print('Check folder for {}.html'.format(table))


    def deleteDB(self, db_name):
        delete_db_query = text('DROP DATABASE ' + db_name)
        
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", module = "sqlalchemy")
            self.connection.execute(delete_db_query)
