import pymysql

class conn():
    def __init__(self):
        self.con=pymysql.connect(host="localhost", user="root", password="", db="crime_scene_detection", port=3306)
        self.cu= self.con.cursor()
    def nonreturn(self,a):
        # self.con = pymysql.connect(host="localhost", user="root", password="", db="sentiment", port=3306)
        # self.cu = self.con.cursor()
        self.cu.execute(a)
        self.con.commit()
        return "ok"

    def mid(self,a):
        # self.con = pymysql.connect(host="localhost", user="root", password="", db="sentiment", port=3306)
        # self.cu = self.con.cursor()
        self.cu.execute(a)
        f=self.cu.fetchone()
        print(f[0])
        if f[0] is None:
            print(f)
            id=1
        else:
            id=f[0]+1
        return id
    def selectall(self,a):
        # self.con = pymysql.connect(host="localhost", user="root", password="", db="sentiment", port=3306)
        # self.cu = self.con.cursor()
        self.cu.execute(a)
        res=self.cu.fetchall()
        return res
    def selectone(self,a):
        # self.con = pymysql.connect(host="localhost", user="root", password="", db="sentiment", port=3306)
        # self.cu = self.con.cursor()
        self.cu.execute(a)
        res =self.cu.fetchone()
        return (res)
    def jsonselect(self,a):
        # self.con = pymysql.connect(host="localhost", user="root", password="", db="sentiment", port=3306)
        # self.cu = self.con.cursor()
        self.cu.execute(a)
        res=self.cu.fetchall()
        return res,self.cu

