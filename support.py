import sqlite3


class DDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()  # создаем класс курсора

    def create_db(self):
        conn = sqlite3.connect("CGF.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS user(
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
        conn.commit()
        conn.close()

    def insert(self, wrs_user, user, departments, mtnb, cpu, ram, video, date, changes, ip_address, MAC, display,
               disk_usage,
               additional_info, os_version, nomachine):
        conn = sqlite3.connect("CGF.db")
        cur = conn.cursor()
        # the NULL parameter is for the auto-incremented id
        cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (
                        wrs_user, user, departments, mtnb, cpu, ram, video, date, changes, ip_address, MAC, display,
                        disk_usage,
                        additional_info, os_version, nomachine))
        conn.commit()
        conn.close()

    def view(self):
        conn = sqlite3.connect("CGF.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(self,wrs_user="", user="", departments="", mtnb="", cpu="", ram="", video="", date="", changes="",
               ip_address="",
               MAC="", display="", disk_usage="",
               additional_info="", os_version="", nomachine=""):
        conn = sqlite3.connect("CGF.db")
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM book WHERE wrs_user = ? OR user = ? OR departments = ? OR mtnb=? OR cpu=? OR ram=? OR video=? OR data=? OR changes=?OR ip_address = ? OR MAC=?"
            "OR display=? OR disk_usage=? OR additional_info=? OR os_version=? OR nomachine=?",
            (wrs_user, user, departments, mtnb, cpu, ram, video, date, changes, ip_address, MAC, display, disk_usage,
             additional_info, os_version, nomachine))
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(self,id):
        conn = sqlite3.connect("CGF.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def update(self,id, wrs_user, user, departments, mtnb, cpu, ram, video, date, changes, ip_address, MAC, display,
               disk_usage,
               additional_info, os_version, nomachine):
        conn = sqlite3.connect("CGF.db")
        cur = conn.cursor()
        cur.execute(
            "UPDATE book SET wrs_user = ?, user = ?, departments = ?, mtnb=?,cpu=?,ram=?,video=?,date=?,changes=?,ip_address=?,MAC=?,display=?,"
            "disk_usage=?,additional_info=?,os_version=?,nomachine=? WHERE id = ?",
            (
                wrs_user, user, departments, mtnb, cpu, ram, video, date, changes, ip_address, MAC, display,
                disk_usage,
                additional_info, os_version, nomachine, id))
        conn.commit()
        conn.close()

    create_db()
