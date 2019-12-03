import mysql.connector
import os, time
from mysql.connector import Error
from datetime import date

class accesSql:

    host = ''
    user = ''
    __passwd = ''
    db = ''

    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.__passwd = passwd
        self.db = db

    def cleanTerminal():
        os.system ("clear")

    def insertUsers(self, email, name, password):
        try:
            connection = mysql.connector.connect(host = self.host, user = self.user, passwd = self.__passwd, db = self.db)
            mySql_insert_query = """INSERT INTO users VALUES("{}", "{}","{}", false);""".format(email, name, password)
            cursor = connection.cursor()
            result = cursor.execute(mySql_insert_query)
            connection.commit()
            print("Inserted data")
            cursor.close()
            return True

        except mysql.connector.Error as error:
            print("error, data no inserted")
            print(error)
            return False

        finally:
            if(connection.is_connected()):
                connection.close()
                print("close connection")
                accesSql.cleanTerminal()
                

    def insertAC(self, id, temp, status):
            try:
                connection = mysql.connector.connect(host = self.host, user = self.user, passwd = self.__passwd, db = self.db)
                mySql_insert_query = """INSERT INTO ac VALUES("{}", "{}","{}");""".format(id, temp, status)
                cursor = connection.cursor()
                result = cursor.execute(mySql_insert_query)
                connection.commit()
                print("Inserted data")
                cursor.close()

            except mysql.connector.Error as error:
                print("error, data no inserted")
                print(error)

            finally:
                if(connection.is_connected()):
                    connection.close()
                    print("close connection")
                    accesSql.cleanTerminal()
                    
    def insertRegForHourr(self, id_ac, temp, status, motion, sended):
        try:

            connection = mysql.connector.connect(host = self.host, user = self.user, passwd = self.__passwd, db = self.db)
            mySql_insert_query = """INSERT INTO regforhour VALUES("{}", "{}",  {},"{}", "{}", "{}");""".format(id_ac, temp, "null", status, motion, sended)
            cursor = connection.cursor()
            result = cursor.execute(mySql_insert_query)
            connection.commit()
            print("Inserted data")
            cursor.close()

        except mysql.connector.Error as error:
            print("error, data no inserted")
            print(error)

        finally:
            if(connection.is_connected()):
                connection.close()
                print("close connection")
                accesSql.cleanTerminal() 


    def insertRegForHour(self, id_ac, temp, status, motion):
        try:

            connection = mysql.connector.connect(host = self.host, user = self.user, passwd = self.__passwd, db = self.db)
            mySql_insert_query = """INSERT INTO regforhour VALUES("{}", "{}", {},"{}", "{}");""".format(id_ac, temp, "NOW()", status, motion)
            cursor = connection.cursor()
            result = cursor.execute(mySql_insert_query)
            connection.commit()
            print("Inserted data")
            cursor.close()
            return True

        except mysql.connector.Error as error:
            print("error, data no inserted")
            print(error)
            time.sleep(5)
            return False

        finally:
            if(connection.is_connected()):
                connection.close()
                print("close connection")
                accesSql.cleanTerminal()  

    def insertRegForDay(self, date, prom, time_on):
        try:

            connection = mysql.connector.connect(host = self.host, user = self.user, passwd = self.__passwd, db = self.db)
            mySql_insert_query = """INSERT INTO regforday VALUES("{}", "{}", "{}");""".format(date, prom, time_on)
            cursor = connection.cursor()
            result = cursor.execute(mySql_insert_query)
            connection.commit()
            print("Inserted data")
            cursor.close()

        except mysql.connector.Error as error:
            print("error, data no inserted")
            print(error)

        finally:
            if(connection.is_connected()):
                connection.close()
                print("close connection")
                accesSql.cleanTerminal()               
                
    def selectUsers(self):
       # """"Puede hacer un select general a todas las tablas""""
        try:
            connection = mysql.connector.connect(host=self.host, user=self.user, passwd=self.__passwd, db=self.db)
            sql_query = "SELECT * FROM users;"
            cursor = connection.cursor()
            cursor.execute(sql_query)
            data = cursor.fetchall()
            return data
        except Error as e:
            print("Error reading data from table {}".format(e))
        # finally:
        #     if(connection.is_connected()):
        #         connection.close()
        #         print("close connection")
        #         accesSql.cleanTerminal()
    
    def deleteRegforHour(self, date):
        try:
            sql_query = "SELECT * FROM regforhour;"
            cursor.execute(sql_query)
            data = cursor.fetchall()
            connection = mysql.connector.connect(host=self.host, user=self.user, passwd=self.__passwd, db=self.db)
            cursor = connection.cursor()
            sql_query = "DELETE FROM regforhour WHERE SUBSTRING(date, 1, 10) = '{}';".format(date)
            cursor.execute(sql_query)
            connection.commit()
            if(len(data) == 0):
                print("Deleted succesefully...")

        except mysql.connector.Error as error:
            print("Failed to delete data : {}".format(error))
        finally:
            if(connection.is_connected):
                connection.close()
                print("close connection")
                accesSql.cleanTerminal()

    def selectRegforhour(self):
        try:
            connection = mysql.connector.connect(host=self.host, user=self.user, passwd=self.__passwd, db=self.db)
            cursor = connection.cursor()
            sql_query = "SELECT * FROM regforhour WHERE id_ac = '{}'".format("G81")
            cursor.execute(sql_query)
            data = cursor.fetchall()
            return data
        except Error as e:
            print("Error reading data from table")
        finally:
            if(connection.is_connected):
                connection.close()
                print("close connection")
                accesSql.cleanTerminal()
    def selectUsersad(self, email):
       # """"Puede hacer un select general a todas las tablas""""
        try:
            connection = mysql.connector.connect(host=self.host, user=self.user, passwd=self.__passwd, db=self.db)
            sql_query = "SELECT * FROM users WHERE email = '{}';".format(email)
            cursor = connection.cursor()
            cursor.execute(sql_query)
            data = cursor.fetchall()
            return data
        except Error as e:
            print("Error reading data from table {}".format(e))

    def selecAc(self):
       # """"Puede hacer un select general a todas las tablas""""
        try:
            connection = mysql.connector.connect(host=self.host, user=self.user, passwd=self.__passwd, db=self.db)
            sql_query = "SELECT * FROM ac;"
            cursor = connection.cursor()
            cursor.execute(sql_query)
            data = cursor.fetchall()
            return data
        except Error as e:
            print("Error reading data from table {}".format(e))
    def deleteac(self, id_ac):
        try:
            connection = mysql.connector.connect(host=self.host, user=self.user, passwd=self.__passwd, db=self.db)
            cursor = connection.cursor()
            sql_query = "DELETE FROM ac WHERE id_ac = '{}';".format(id_ac)
            cursor.execute(sql_query)
            connection.commit()
            sql_query = "SELECT * FROM ac;"
            cursor.execute(sql_query)
            data = cursor.fetchall()
            if(len(data) == 0):
                print("Deleted succesefully...")
            return True    

        except mysql.connector.Error as error:
            print("Failed to delete data : {}".format(error))
        finally:
            if(connection.is_connected):
                connection.close()
                print("close connection")
                accesSql.cleanTerminal()
    
    def acUpdate(self, id_ac):
        try:
            connection = mysql.connector.connect(host=self.host, user=self.user, passwd=self.__passwd, db=self.db)
            cursor = connection.cursor()
            data = self.selecAc()
            for d in data:
                if(d[2] == 1 and d[0] == id_ac):
                    sql_query = "UPDATE ac SET  status = 0 WHERE id_ac = '{}';".format(id_ac)
                    cursor.execute(sql_query)
                    connection.commit()
                    sql_query = "SELECT * FROM ac;"
                    cursor.execute(sql_query)
                    data = cursor.fetchall()
                else:
                    sql_query = "UPDATE ac SET  status = 1 WHERE id_ac = '{}';".format(id_ac)
                    cursor.execute(sql_query)
                    connection.commit()
                    sql_query = "SELECT * FROM ac;"
                    cursor.execute(sql_query)
                    data = cursor.fetchall()
                    
            if(len(data) == 0):
                print("Deleted succesefully...")
            return True    

        except mysql.connector.Error as error:
            print("Failed to delete data : {}".format(error))
        finally:
            if(connection.is_connected):
                connection.close()
                print("close connection")
                accesSql.cleanTerminal()
