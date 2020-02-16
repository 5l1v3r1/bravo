class Postgres:

    """
    Postgres constructor
    """
    def __init__(self, database):
        self.database = database

    """
    Initialize the database, create the tables
    """
    def initialize(self):
        self.database.execute("create extension if not exists cube;")
        self.database.execute("drop table if exists faces")
        self.database.execute("create table faces (id serial, person_id serial, image_id serial, vec_low cube, vec_high cube);")
        self.database.execute("create index faces_vec_idx on faces (vec_low, vec_high);")