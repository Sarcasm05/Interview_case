import sqlite3

class AdoptBranch:
    def __init__(self):
        self.connection =  sqlite3.connect(db='activeDB', passwd='HavanaClub')
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self.cursor
    def __exit__(self, type, value, traceback):
        self.connection.commit()

    def create_db(name_db='resource/infovpsdb'):
        conn = sqlite3.connect(name_db)
        cursor = conn.cursor()

        cursor.execute(
                """CREATE TABLE infohost (id integer primary key autoincrement, / 
                                namegase text, prices text, path text)""")

    @staticmethod
    def select_path(prices):
        return """SELECT * FROM infohost where price='%s'" % (prices)""" % (prices)

    @staticmethod
    def  insert_gaseline(gaseline, price, path):
        return """INSERT INTO infohost('%s', '%s', '%s')""" % (gaseline,price,path)

