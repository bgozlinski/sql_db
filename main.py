from src.connect import PostgresDB

def execute_sql_file(file_path):
    """
    Executes an SQL query stored in a file.

    :param file_path: Path to the SQL file.
    :param params: Parameters for the SQL query, if required.
    """
    db = PostgresDB()
    db.connect()
    cursor = db.conn.cursor()

    with open(file_path, 'r') as file:
        sql_query = file.read()
        cursor.execute(sql_query)

    results = cursor.fetchall()
    for result in results:
        print(result)

    cursor.close()
    db.close()


def main():
    sql_file = 'queries/query_10.sql'
    execute_sql_file(sql_file)


if __name__ == '__main__':
    main()
