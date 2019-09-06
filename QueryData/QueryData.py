class QueryData:
    def __init__(self,db):
        self.db = db

    def selectQueryMethod(self,query):
        try:
            self.query = query
            cursor = self.db.cursor()
            cursor.execute(query)
            return self.parseData(cursor)
        except:
            return []

    def parseData(self,cursor):
        data = cursor.fetchall()
        listOfKeyValData = [ dict(zip([key[0] for key in cursor.description],row)) for row in data ]
        cursor.close()
        return listOfKeyValData

    def insertAndUpdateQueryMethod(self,query,val):
        try:
            self.query = query
            cursor = self.db.cursor()
            cursor.execute(query,val)
            self.db.commit()
            return { "Inserted Row": cursor.rowcount }
        except:
            return { "Inserted Row":0 }
    
    def insertOrUpdateMany(self,query,values):
        try:
            # self.query = query
            cursor = self.db.cursor()
            cursor.executemany(query,val)
            self.db.commit()
            return { "Inserted Row": cursor.rowcount }
        except:
            return { "Inserted Row":0 } 




