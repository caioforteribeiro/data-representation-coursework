import mysql.connector
class catsDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="datarepresentation"
        )

    #Create
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into cats (name, age, breed) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid
    
    #Get all
    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from cats"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        return returnArray
    
    #Find by ID
    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from cats where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)
    
    #Update
    def update(self, values):
        cursor = self.db.cursor()
        sql="update cats set name= %s, age=%s, breed=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()

    #Delete
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from cats where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id','name','age','breed']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
    
    catsDAO = catsDAO()

    