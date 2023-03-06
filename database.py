from flask import g
import sqlite3

def connect_db():
    sql = sqlite3.connect('/home/marcin/Documents/Projects/MemberAPI//members.db') #location to your db file
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db