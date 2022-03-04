import sqlite3 as sql

DB_PATH = "F:\\Examenes Entrevistas\\Intercorp Retail\\Prueba_Python_Cloud\\database\\client.db"



def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE client (
        ID integer,
        name_client text,
        age integer,
        country text,
        score float

    )""")
    conn.commit()
    conn.close()

def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        (1001,"Fabian",24,"Peru",8.5),
        (1002,"Aracely",25,"Peru",9.5),
        (1003,"Benito",22,"Chile",7.5),
        (1004,"Pedro",28,"España",9.6),
        (1005,"Carlos",30,"Inglaterra",6.5)
    ]
    cursor.executemany("""INSERT INTO client VALUES(?,?,?,?,?)""",data)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    createDB()
    addValues()

