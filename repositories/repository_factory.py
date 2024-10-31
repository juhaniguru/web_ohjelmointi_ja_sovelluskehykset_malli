import os

from repositories.log_postgres_repo import LogPostgresRepo
from repositories.users_mysql_repository import UsersMysqlRepository
from repositories.users_postgres_repository import UsersPostgresRepository


def users_repository_factory(con):

    return UsersMysqlRepository(con)

def log_repository_factory(con):
    return LogPostgresRepo(con)

def vehicles_repository_factory():
    pass