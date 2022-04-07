import sqlite3


class DDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()  # создаем класс курсора
        self.__db.sqlite3.connect("CGF.db")
        self.__cur.fetchall()

    def create_db(self):
        self.__cur.execute('''CREATE TABLE IF NOT EXISTS user(
       wrs_user TEXT,
       user TEXT,
       departments TEXT,
       mtnb TEXT,
       cpu TEXT,
       ram TEXT,
       video TEXT,
       date DATETIME,
       changes INT,
       ip_address INT,
       MAC INT ,
       displays TEXT,
       disk_usage INT,
       additional_info TEXT,
       os_version TEXT,
       nomachine TEXT
       )
        
        ''')
        self.__db.commit()
        self.__db.close()

    def insert(self, wrs_user, user, departments, mtnb, cpu, ram, video, date, changes, ip_address, MAC, display,
               disk_usage,
               additional_info, os_version, nomachine):
        self.__cur.cursor()
        # the NULL parameter is for the auto-incremented id
        self.__cur.execute("INSERT INTO CGF VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                           (
                               wrs_user, user, departments, mtnb, cpu, ram, video, date, changes, ip_address, MAC,
                               display,
                               disk_usage,
                               additional_info, os_version, nomachine))
        self.__db.commit()
        self.__db.close()

    def view(self):
        self.__db.sqlite3.connect("CGF.db")
        self.__cur.cursor()
        self.__cur.execute("SELECT * FROM CGF")
        self.__cur.fetchall()
        self.__db.close()
        return self.__cur.fetchall()

    def search(self, wrs_user="", user="", departments="", mtnb="", cpu="", ram="", video="", date="", changes="",
               ip_address="",
               MAC="", display="", disk_usage="",
               additional_info="", os_version="", nomachine=""):
        self.__db.sqlite3.connect("CGF.db")
        self.__cur.cursor()
        self.__cur.execute(
            "SELECT * FROM CGF WHERE wrs_user = ? OR user = ? OR departments = ? OR mtnb=? OR cpu=? OR ram=? OR video=? OR data=? OR changes=?OR ip_address = ? OR MAC=?"
            "OR display=? OR disk_usage=? OR additional_info=? OR os_version=? OR nomachine=?",
            (wrs_user, user, departments, mtnb, cpu, ram, video, date, changes, ip_address, MAC, display, disk_usage,
             additional_info, os_version, nomachine))
        self.__cur.fetchall()
        self.__db.close()
        return self.__cur.fetchall()

    def delete(self, id):
        self.__db.sqlite3.connect("CGF.db")
        self.__cur.cursor()
        self.__cur.execute("DELETE FROM CGF WHERE id = ?", (id,))
        self.__db.commit()
        self.__db.close()

    def update(self, id, wrs_user, user, departments, mtnb, cpu, ram, video, date, changes, ip_address, MAC, display,
               disk_usage,
               additional_info, os_version, nomachine):
        self.__db.sqlite3.connect("CGF.db")
        self.__cur.cursor()
        self.__cur.execute(
            "UPDATE CGF SET wrs_user = ?, user = ?, departments = ?, mtnb=?,cpu=?,ram=?,video=?,date=?,changes=?,ip_address=?,MAC=?,display=?,"
            "disk_usage=?,additional_info=?,os_version=?,nomachine=? WHERE id = ?",
            (
                wrs_user, user, departments, mtnb, cpu, ram, video, date, changes, ip_address, MAC, display,
                disk_usage,
                additional_info, os_version, nomachine, id))
        self.__db.commit()
        self.__db.close()



