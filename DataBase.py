import pymysql as mysql
from threading import Thread
from time import sleep 
from CommonVariables.commonvariables import *

class DataBase():
    def __init__(self):
        self.mysql_db = mysql.connect(host='127.0.0.1',user=userName, password=password, database=dbName)  
        Thread(target=self.reconnect).start()

    def reconnect(self):
        while True:
            sleep(60)
            # print("New Connection")
            self.mysql_db.close()
            self.mysql_db.ping(reconnect=True) 
            # self.mysql_db = mysql.connect(host='127.0.0.1',user='root', password='password', database="dbtest1")

    def cursor(self):
        return self.mysql_db
