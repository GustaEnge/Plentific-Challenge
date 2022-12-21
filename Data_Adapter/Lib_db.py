import os,getpass
import re
from sqlite3.dbapi2 import connect
import sys
import sqlite3
from copy import Error
class DataBase:
    dataBase = "db_mock"
    sql_columns = "id INTEGER PRIMARY KEY AUTOINCREMENT ,firstName TEXT, lastName TEXT, company TEXT,phone TEXT, email TEXT,password TEXT,vat TEXT NOT NULL UNIQUE, country TEXT,address TEXT,zipcode TEXT,city TEXT,website TEXT,tax_country INTEGER,language TEXT,terms INTEGER,force TEXT,shareCapital DOUBLE, signedUp TEXT,account_id INTENGER,api_id TEXT, apiKey TEXT, seq INTEGER, created_at TEXT"
    sql_create_table_users_sqlite = '''CREATE TABLE IF NOT EXISTS tb_users(%s);'''% sql_columns
    sql_insert_table_users = '''INSERT INTO tb_users(company,firstName,lastName,email,password,country,vat,address,zipcode,city,website,shareCapital,phone,signedUp,account_id,api_id, apiKey,seq) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,False,Null,Null,Null,Null);'''
    sql_insert_table_users_sqlite = '''INSERT INTO tb_users(firstName,lastName,company,email,password,vat,country,address,zipcode,city,website,tax_country,language,terms,force,shareCapital,phone,signedUp,account_id,api_id,apiKey,seq,created_at) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',%d,'%s','%s','%s',%d,'%s',0,Null,Null,Null,Null,datetime('now','localtime'));'''
    sql_update_table_users_sqlite = '''UPDATE tb_users SET account_id = %d,api_id = '%s',apiKey = '%s', seq = %d, signedUp = 1 WHERE id = %d'''

    conn = None
    def __init__(self,type) -> None:
        self.type = type
        self.conn = ""
        self.db = f"/Users/gustavocunha/Github/ZyteProject/DataSet_Adapter/sqlite/"
        self.connectDB()
        
        
        
    def connectDB(self):
        # if self.type == 'mysql':
        #     try:
                
        #         self.conn = mysql.connector.connect(
        #             host="localhost",
        #             user="root",
        #             password = "GxTaTu@9427",
        #             db = self.dataBase
        #         )
        #         cursor = self.conn.cursor()
        #         cursor.execute(self.sql_create_db)
        #         cursor.execute(self.sql_create_table_users)
                
        #     except mysql.connector.Error as e:
        #         print(e)                        
        if self.type == 'sqlite':
            try:
                self.conn = sqlite3.connect(self.db+'db_mock.db',10)
                cursor = self.conn.cursor()
                cursor.execute(self.sql_create_table_users_sqlite)
            except Error as e:
                print(e)

    def insertDB(self,list_var):
       
        instruction = ""

        if type(list_var) == dict: instruction = self.sql_insert_table_users_sqlite % (list_var['firstName'],list_var['lastName'], list_var['company'],list_var['email'],list_var['password'],list_var['vat'],list_var['country'],list_var['address'],list_var['zipcode'],list_var['city'],list_var['website'],int(list_var['tax_country']),list_var['language'],list_var['terms'],list_var['force'],list_var['shareCapital'],list_var['phone'])
         #prevents sql execution from throwing syntax error ' (single quote inside some attributes)
        else: instruction =  re.sub("'","''",self.sql_insert_table_users_sqlite % list_var)
        
        cursor = self.conn.cursor()
        cursor.execute(instruction)
        self.conn.commit()
        self.conn.close()
    def updateDB(self, list_var):
        cursor = self.conn.cursor()
        instruction =  self.sql_update_table_users_sqlite % tuple(list_var)
        cursor.execute(instruction)
        self.conn.commit()
        self.conn.close()  
    def insertManyDB(self,data):
        if self.type == "sqlite":
            c = self.conn.cursor()
            for item in data:
                query = self.sql_insert_table_users_sqlite % item
                c.execute(query)   
        else:
            with self.conn.cursor() as cursor:
                instruction =  self.sql_insert_table_users  
                cursor.executemany(instruction,data)
        self.conn.commit()
        self.conn.close()

    def readAccount(self,id_account):
        data = {}
        instruction =  f"SELECT * FROM tb_users WHERE id = {id_account}"
        if self.type == "sqlite":
            c = self.conn.cursor()
            c.execute(instruction)
            keys = [i[0] for i in c.description]
            values = c.fetchall()[0]
            data = {keys[i]:values[i] for i in range(len(keys))}
        else:
            with self.conn.cursor() as cursor:
                cursor.execute(instruction)
                keys = [i[0] for i in cursor.description]
                values = cursor.fetchall()[0]
                data = {keys[i]:values[i] for i in range(len(keys))}
                
        self.conn.commit()
        self.conn.close()
        return data
        
    def getLastID(self):
        instruction = 'SELECT id FROM tb_users ORDER BY rowid DESC LIMIT 1;'
        c = self.conn.cursor()
        c.execute(instruction)
        data = c.fetchone()
        self.conn.commit()
        self.conn.close()

        return data

def main():
    db = DataBase('sqlite')
    print(db.readAccount("1"))

if __name__=="__main__":
    main()