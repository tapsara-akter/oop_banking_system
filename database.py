import mysql.connector as conn


class MySQLdb:

    def connect_mysql(self, host="localhost", user='root', password='', database=''):
        try:
            if database != '':
                mydb = conn.connect(
                    host=host,  # 127.0.0.1
                    user=user,
                    password=password,
                    database=database
                )
            else:
                mydb = conn.connect(
                    host=host,  # 127.0.0.1
                    user=user,
                    password=password,
                )
            print(mydb)
            return mydb
        except Exception as e:
            print(e)

    def create_database(self, dbname):
        try:
            connection = self.connect_mysql()
            cursor = connection.cursor()
            sql = "CREATE DATABASE " + dbname
            cursor.execute(sql)
            cursor.close()
            connection.close()
        except Exception as e:
            print(e)

    def create_table(self, table_name):
        try:
            connection = self.connect_mysql(database='bank')
            cursor = connection.cursor()
            sql = "CREATE TABLE " + table_name + " (id integer, name varchar(255), account float)"
            cursor.execute(sql)
            cursor.close()
            connection.close()
        except Exception as e:
            print(e)

    def insert_data(self, table_name):
        try:
            connection = self.connect_mysql(database='bank')
            cursor = connection.cursor()
            sql = "INSERT INTO " + table_name + "(id, name, account) VALUES(1, 'Shumon', '10000')"
            sql2 = "INSERT INTO " + table_name + "(id, name, account) VALUES(2,'Alim', '1050000')"
            sql3 = "INSERT INTO " + table_name + "(id, name, account) VALUES(3, 'Tarek', '53000')"
            # val = (id, name, account)
            for i in [sql, sql2, sql3]:
                cursor.execute(i)
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as e:
            print(e)

    def show_data(self, table_name):
        try:
            connection = self.connect_mysql(database='bank')
            cursor = connection.cursor()
            sql = "SELECT * FROM " + table_name
            cursor.execute(sql)
            resutl = cursor.fetchall()
            for i in resutl:
                print(i)
            cursor.close()
            connection.close()
        except Exception as e:
            print(e)


mysql_handl = MySQLdb()
mysql_handl.create_database('bank')
mysql_handl.create_table('customer')
mysql_handl.insert_data('customer')
mysql_handl.show_data('customer')