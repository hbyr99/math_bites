from mysql.connector import connect, Error

class DB_Func:
    def __init__(self, host, user):
        self.host = host
        self.user = user
        self.connection = connect(
            host=self.host,
            user=self.user,
            #password=getpass("Enter password: "),
        )


    def createDB(self, db_name):
        try:
            create_db_query = 'CREATE DATABASE IF NOT EXISTS ' + db_name + '; '
            with self.con.cursor() as cursor:
                cursor.execute(create_db_query)

                self.connection = connect(
                    host = self.host,
                    user = self.user,
                    #password=getpass("Enter password: "),
                    database = db_name,
                )
                connection.commit()

        except Error as e:
            print(e)

    def addEntry(self, table, number):
        create_table_query = """
        CREATE TABLE [IF NOT EXISTS] {} (
            number INT PRIMARY KEY,
            appearances INT UNSIGNED DEFAULT 1
        )
        """.format(table)
        insert_entry = """
        INSERT INTO {} (number) 
            VALUES number
            ON DUPLICATE KEY UPDATE appearances = appearances + 1 
        """.format(table)

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(create_table_query)
                cursor.execute(insert_entry)
                connection.commit()
        
        except Error as e:
            print(e)