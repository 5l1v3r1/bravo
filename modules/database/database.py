import postgresql
import mysql.connector
from mysql.connector import pooling
from config.database import Database as Config
from modules.database.adapters.mysql import Mysql
from modules.database.adapters.postgres import Postgres


class Database:

    # Save file to adapters
    @staticmethod
    def save(database, profile):
        if Config().type() == 'mysql':
            Mysql(database).save(profile)
        elif Config().type() == 'postgres':
            Postgres(database).save(profile)

    # Add to indexed
    @staticmethod
    def indexed(database, profile_id):
        if Config().type() == 'mysql':
            Mysql(database).indexed(profile_id)
        elif Config().type() == 'postgres':
            Postgres(database).indexed(profile_id)

    # check if repo has been indexed
    @staticmethod
    def has_been_indexed(database, profile_id):
        if Config().type() == 'mysql':
            Mysql(database).has_been_indexed(profile_id)
        elif Config().type() == 'postgres':
            Postgres(database).has_been_indexed(profile_id)

    # initialize database
    @staticmethod
    def initialize(database):
        if Config().type() == 'mysql':
            Mysql(database).initialize()
        elif Config().type() == 'postgres':
            Postgres(database).initialize()

    # Connect to the database
    @staticmethod
    def connect():
        try:
            if Config().type() == 'mysql':
                connector = mysql.connector.pooling.MySQLConnectionPool(**Config().mysql())
            elif Config().type() == 'postgres':
                connector = postgresql.open(Config().postgres())

            return connector
        except Exception as e:
            return
