from fastapi import APIRouter, HTTPException
from fastapi.utils import *
import sqlite3

router = APIRouter()


def getConnection():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    return conn, c


def getResponseDict(query: str) -> dict:
    """
    This method return the info from a database in a better way, so that the column name is the key and the value is the value.

    :param query: The normal SQL query
    :return: A dictionary with the column name as the key and the value as the value
    """
    conn, c = getConnection()
    c.execute(query)
    data = c.fetchall()
    column_names = [description[0] for description in c.description]
    response = {}
    for i in range(len(data)):
        response[i] = {}
        for j in range(len(data[i])):
            response[i][column_names[j]] = data[i][j]
    if len(response) == 0:
        raise HTTPException(status_code=404, detail="No data found")
    if len(response) == 1:
        return response[0]
    return response


@router.get("/connect")
def connect() -> bool:
    conn, c = getConnection()
    return conn is not None


@router.get("/create")
def create_table() -> bool:
    conn, c = getConnection()
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS users (
            username text,
            password text
        )""")
        conn.commit()
    except Exception as e:
        print(e)
        return False
    return True


@router.get("/list")
def listTables() -> str:
    conn, c = getConnection()
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    fetchall = c.fetchall()
    fetchall = [i[0] for i in fetchall]
    return str(fetchall)


@router.put("/add")
def add_user(username: str, password: str) -> bool:
    conn, c = getConnection()
    try:
        c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        conn.commit()
    except Exception as e:
        print(e)
        return False
    return True


@router.patch("/update")
def update_user(username: str, password: str) -> bool:
    conn, c = getConnection()
    try:
        c.execute("UPDATE users SET password=? WHERE username=?", (password, username))
        conn.commit()
    except Exception as e:
        print(e)
        return False
    return True


@router.delete("/delete")
def delete_user(username: str) -> bool:
    conn, c = getConnection()
    try:
        c.execute("DELETE FROM users WHERE username=?", (username,))
        conn.commit()
    except Exception as e:
        print(e)
        return False
    return True


@router.get("/get")
def get_user(username: str) -> dict:
    return getResponseDict("SELECT * FROM users WHERE username='{}'".format(username))


@router.get("/getall")
def get_all_users() -> dict:
    return getResponseDict("SELECT * FROM users")


@router.delete("/deleteall")
def delete_all_users(you_sure:bool=False) -> bool:
    if not you_sure:
        raise HTTPException(status_code=403, detail="You must be sure")
    conn, c = getConnection()
    try:
        c.execute("DELETE FROM users")
        conn.commit()
    except Exception as e:
        print(e)
        return False
    return True