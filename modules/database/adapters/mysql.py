class Mysql:

    """
    Mysql constructor
    """
    def __init__(self, database):
        self.database = database

    """
    Initialize the database, create the tables
    """
    def initialize(self):
        createFaceEncodingsTable = """
            CREATE TABLE IF NOT EXISTS `face_encodings` (
                `id` int unsigned NOT NULL AUTO_INCREMENT,
                `person_id` int DEFAULT NULL,
                `image_id` int DEFAULT NULL,
                `created_at` datetime DEFAULT NULL,
                PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;  
        """

        for attempt in range(5):
            try:
                cur = self.database.cursor()
                cur.execute(createFaceEncodingsTable)

                # Add encoding columns
                for encoding in range(1, 129):
                    cur.execute(
                        "alter table face_encodings add column encoding_%s decimal(10,0) NOT NULL" % encoding
                    )
            except Exception as e:
                pass
