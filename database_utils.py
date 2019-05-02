import sqlite3
def load_path():
    path=input('Enter the path to db file with api key')
    return path
def loadConnection():
    #Enter the path for sql file 
    path=load_path()
    path=path+'\\'+'keys.db'
    Connection=sqlite3.connect(path)
    cursor=Connection.cursor()
    return(Connection,cursor)
def fetch_key():
    Connection,cursor=loadConnection()
    query='select api_key from api_store'
    cursor.execute(query)
    key,=cursor.fetchone()
    return(key)
