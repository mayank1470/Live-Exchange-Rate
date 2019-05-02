import sqlite3
def load_path():
    path=input('Enter the path to save/Read file: ')
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
def save_key(api_key):
    query='insert into api_store(api_key) values(?)'
    # query=query.format(api_key)
    print('Executing-->',query)
    Connection,cursor=loadConnection()
    cursor.execute(query,(api_key,))
    Connection.commit()
    cursor.close()
    Connection.close()

