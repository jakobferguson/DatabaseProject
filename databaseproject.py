import sqlite3 as db
from getpass import getpass


def genTable():
        con = db.connect("tuple.db")
        cur = con.cursor()
        # Create user table
        command1 = """CREATE TABLE IF NOT EXISTS
        user(user_id INTEGER PRIMARY KEY, full_name TEXT, password TEXT, weight INTEGER, g_weight INTEGER, g_macros INT)"""
        cur.execute(command1)

        # Create the equipment (eqp) table
        command2 = """CREATE TABLE IF NOT EXISTS
        eqp(eqp_name TEXT PRIMARY KEY)"""
        cur.execute(command2)

        # Create the equipment owned (eqp_owned) table
        command3 = """CREATE TABLE IF NOT EXISTS
        eqp_owned(user_id INTEGER, eqp_name TEXT, 
                FOREIGN KEY(user_id) REFERENCES user(user_id), 
                FOREIGN KEY(eqp_name) REFERENCES eqp(eqp_name))"""
        cur.execute(command3)

        # Create the exercise table
        command4 = """CREATE TABLE IF NOT EXISTS
        exercise(exc_name TEXT PRIMARY KEY, instruction TEXT, type TEXT, eqp_name TEXT,
                FOREIGN KEY(eqp_name) REFERENCES eqp(eqp_name))"""
        cur.execute(command4)

        # Create the muscle used (m_used) table
        command5 = """CREATE TABLE IF NOT EXISTS
        m_used(exc_name TEXT, muscle TEXT,
        FOREIGN KEY(exc_name) REFERENCES exercise(exc_name),
        PRIMARY KEY(exc_name, muscle))"""
        cur.execute(command5)

        # Create the workout table
        command6 = """CREATE TABLE IF NOT EXISTS
        workout(wid INTEGER PRIMARY KEY, w_name TEXT, type TEXT, modifiable TEXT, user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES user(user_id))"""
        cur.execute(command6)

        # Create the health log table
        command7 = """CREATE TABLE IF NOT EXISTS
        health_log(log_id INTEGER PRIMARY KEY, user_id INTEGER, weight INTEGER,
                FOREIGN KEY(user_id) REFERENCES user(user_id))"""
        cur.execute(command7)

        # Create the lifting log table
        command8 = """CREATE TABLE IF NOT EXISTS
        lift_log(log_id INTEGER PRIMARY KEY, user_id INTEGER, exc_name TEXT, weight INTEGER, sets INTEGER, reps INTEGER,
                FOREIGN KEY(user_id) REFERENCES user(user_id),
                FOREIGN KEY(exc_name) REFERENCES exercise(exc_name))"""
        cur.execute(command8)
        #create the exc_included table
        command9 = """CREATE TABLE IF NOT EXISTS 
                exc_included(wid INTEGER, exc_name TEXT, exc_sets INTEGER NOT NULL, exc_reps INTEGER NOT NULL,
                PRIMARY KEY (wid, exc_name),
                FOREIGN KEY (wid) REFERENCES workout(wid),
                FOREIGN KEY (exc_name) REFERENCES exercise(exc_name))
                """
        cur.execute(command9)




