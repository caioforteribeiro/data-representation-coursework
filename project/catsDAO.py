import mysql.connector
import dbconfig as cfg


class catsDAO:
    connection=""
    cursor =""
    host=""
    user=""
    password=""
    database=""

    #Initialise
    def __init__(self):
        self.host=cfg.mysql['host']
        self.user=cfg.mysql['user']
        self.password=cfg.mysql['password']
        self.database=cfg.mysql['database']

    #Cursor
    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    #Close connection and cursor
    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    #Create
    def create(self, values):
        cursor = self.getcursor()
        sql="insert into cats (name,age,sex,breed) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
    
    #Get all
    def getAll(self):
        cursor = self.getcursor()
        sql="select * from cats"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray
    
    #Find by ID
    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from cats where id=%s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue
    
    #Update
    def update(self, values):
        cursor = self.getcursor()
        sql="update cats set name= %s,age=%s,breed=%s  where id=%s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    #Delete
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from cats where id=%s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("delete done")

    def convertToDictionary(self, result):
        colnames=["id","name","age","sex","breed"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
    
    catsDAO = catsDAO()

    