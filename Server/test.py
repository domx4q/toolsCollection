import sqlite3


def getConnection():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    return conn, c


def listTables() -> str:
    conn, c = getConnection()
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    fetchall = c.fetchall()
    fetchall = [i[0] for i in fetchall]
    return str(fetchall)


if __name__ == '__main__':
    print(listTables())