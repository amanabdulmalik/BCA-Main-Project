import mysql.connector


class Db:
    def __init__(self):
        self.cnx = mysql.connector.connect(host="localhost",user="root",password="",database="crime_scene_detection")
        self.cur = self.cnx.cursor(buffered=True,dictionary=True)


    def select(self, q):
        self.cur.execute(q)
        return self.cur.fetchall()

    def select_one(self, q):
        self.cur.execute(q)
        return self.cur.fetchone()

    def insert(self, q):
        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.lastrowid

    def update(self, q):
        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.rowcount

    def delete(self, q):
        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.rowcount



