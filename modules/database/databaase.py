import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
from config.database import Database as Config
from modules.database.adapters.mysql import Mysql


class Database:

    # Save file to adapters
    @staticmethod
    def save(database, files):
        if Config().type() == 'mysql':
            Mysql(database).save(files)

    # Add to indexed
    @staticmethod
    def indexed(database, repo_id):
        if Config().type() == 'mysql':
            Mysql(database).indexed(repo_id)

    # check if repo has been indexed
    @staticmethod
    def has_been_indexed(database, repo_id):
        if Config().type() == 'mysql':
            Mysql(database).has_been_indexed(repo_id)

    # Connect to the database
    @staticmethod
    def connect():
        for attempt in range(20):
            try:
                if Config().type() == 'mysql':
                    connector = mysql.connector.pooling.MySQLConnectionPool(**Config().mysql())

                return connector
            except:
                pass

