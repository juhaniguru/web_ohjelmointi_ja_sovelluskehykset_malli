import mysql.connector

from db_conn_factory import con_factory


def get_db_connection(route_handler):
    def wrapper(*args, **kwargs):
        with con_factory() as con:
            # seuraavan funktion eka parametri on con
            return route_handler(con, *args, **kwargs)

    return wrapper