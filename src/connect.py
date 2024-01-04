import psycopg2
from config import config


class PostgresDB:
    """
    A class used to represent a connection to a PostgreSQL database.

    Attributes
    ----------
    conn : psycopg2.extensions.connection
        The PostgreSQL database connection object.

    Methods
    -------
    connect()
        Establishes a connection to the PostgreSQL database using parameters from the config file.

    close()
        Closes the connection to the database.
    """

    def __init__(self):
        """
        Initializes a new instance of the PostgresDB class, setting the conn attribute to None.
        """
        self.conn = None
        self.cur = None

    def connect(self) -> None:
        """
        Establish a connection to the PostgreSQL database.

        This method reads the database configuration using the config module, attempts to establish
        a connection to the database, and prints the database version upon successful connection.

        Raises
        ------
        Exception
            If an error occurs during the connection attempt.
        """

        try:
            params = config()
            print("Connecting to database...")
            self.conn = psycopg2.connect(**params)
            self.cur = self.conn.cursor()
            self.cur.execute('SELECT version()')
            db_version = self.cur.fetchone()
            print(f'Connected to {db_version[0]}')

        except Exception as e:
            print(f"Error connecting to PostgreSQL DB: {e}")
            if self.conn is not None:
                self.conn.close()

        return self.cur

    def close(self) -> None:
        """
        Close the database connection.

        If a connection to the database has been established, this method closes it.
        """
        if self.conn:
            self.conn.close()
            print("Connection closed.")
