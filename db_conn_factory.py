import contextlib
import os
import mysql.connector
import psycopg2

@contextlib.contextmanager
def con_factory():
    con = None
    try:
        print("#######confactory::1")
        _db = os.getenv('DB')

        if _db == 'mysql':
            con = mysql.connector.connect(database='sovelluskehykset_bad1', user='root', password='')
        elif _db == 'postgres':
            con = psycopg2.connect(database='sovelluskehykset_bad1', user='postgres', password='salasana')
        yield con
    finally:
        print("##########confactory::2")
        if con is not None:
            con.close()


