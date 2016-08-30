import pypyodbc
import datetime

class Database:

    def __init__(self,connectionString):
        self.cstring = connectionString

    def save(self,text):
        connection = pypyodbc.connect(self.cstring)
        cursor = connection.cursor()
        sql = "INSERT INTO TEST.dbo.TrackingTable (TimeEntered,Settings) VALUES (?,?)"
        values = [datetime.datetime.now(),text]
        cursor.execute(sql,values)
        connection.commit()
        connection.close()

