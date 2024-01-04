import psycopg2
from connect import PostgresDB


def create_table_from_sql_file(file_name):
    db = PostgresDB()
    cursor = db.connect()

    try:
        with open(file_name, 'r') as f:
            cursor.execute(f.read())
            db.conn.commit()
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    finally:
        db.close()


if __name__ == '__main__':
    create_table_from_sql_file("create_tables.sql")
